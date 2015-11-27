import pandas as pd
import numpy as np
import psycopg2
import requests
import shutil
import boto
from skimage.io import imread,imsave
from skimage.transform import resize
from sklearn.metrics.pairwise import pairwise_distances
from collections import Counter
from binarize import BinarizeArray
import subprocess
import multiprocessing as mp
import re
import os

def test_split(in_val):
	return in_val[0], map(float,in_val[1].replace('{','').replace('}','').split(','))


class DoggyMatchEngine(object):
	def __init__(self, GPU=True):
		self.conn = psycopg2.connect(dbname='dogs', user='ubuntu')
		self.psql = self.conn.cursor()
		self.features = []
		self.GPU = GPU
		self.binar = BinarizeArray()
		self.binar.run()


	def fit(self,user_input,session_id):
		self.session_id=session_id
		if "http" in user_input or "https" in user_input:
			r = requests.get(user_input, stream=True)
			if r.status_code == 200:
				rand_name = 'tmp/img_'+session_id+'.jpg'
				with open(rand_name, 'wb') as f:
					r.raw.decode_content = True
					shutil.copyfileobj(r.raw, f)
					img_file = rand_name 
		else: 
			img_file = user_input

		img = imread(img_file)
		i_size = img.shape
		if i_size[0] < 221 or i_size[1] < 221 or (i_size[2] != 3 and i_size[2] != 4):
			raise Exception('Img too small to process.')
		imgr = resize(img,[221,221])
		img_file = img_file
		imsave(img_file,imgr)
		if self.GPU:
			p = subprocess.check_output(["/OverFeat/bin/linux_64/cuda/overfeat_cuda", "-f", "-l", img_file])
		else:
			p = subprocess.check_output(["/OverFeat/bin/linux_64/overfeat", "-f", "-l", img_file])
		features = p.replace('\n','').replace('1-','').strip(' ').split(' ')[2:]
		features =  [float(x) for x in features]
		if len(features) != 4096:
			raise Exception('Feature size is off.')
		self.user_features = features



	def match(self, user_zip, user_radius, num_matches=10):
		self.psql.execute(
			'''select lng,lat from zipcodes where zip=%s limit 1;  
			''' % user_zip
			)
		lnglat = self.psql.fetchall()
		user_long = lnglat[0][0]
		user_lat = lnglat[0][1]

		self.psql.execute(
			'''select id,features_bin from records where ST_Distance_Sphere(geom, ST_MakePoint(%s, %s))*0.000621371 < %s;  
			''' % (user_long,user_lat,user_radius)
			)
		filtered = self.psql.fetchall()

		#pool = mp.Pool(8)
		#rec_tuple = pool.map(test_split,filtered)
		self.geo_ids_lst = [x[0] for x in filtered]
		self.geo_feature_lst = [x[1] for x in filtered]

		print len(self.geo_feature_lst)
		print self.geo_feature_lst[0]

		sim_scores = pairwise_distances(np.array(self.user_features),np.array(self.geo_feature_lst),'cosine', n_jobs=-1)
		sim_scores = np.array(sim_scores).flatten()
		ids = np.array(self.geo_ids_lst)
		match_inds = sim_scores.argsort()
		min_arr = match_inds[:num_matches]
		self.top10_scores = sim_scores[min_arr]
		self.top10_ids = ids[min_arr]


		ids_subset = [re.sub('_.*','',x) for x in self.top10_ids]
		c_ids = Counter(ids_subset)

		if c_ids.most_common()[0][1] >1:
			dupes = True
		else:
			dupes = False

		data_in = num_matches
		while dupes:
			arr_ids = np.array(ids_subset)
			repeats = np.where(arr_ids==c_ids.most_common()[0][0])
			dup_ind = repeats[0][1]
			new_top_ids = np.delete(self.top10_ids, dup_ind)
			new_top_scores =np.delete(self.top10_scores, dup_ind)
			repl_match_ind = match_inds[data_in]
			self.top10_scores =np.append(new_top_scores, sim_scores[repl_match_ind])
			self.top10_ids =np.append(new_top_ids,ids[repl_match_ind])
			ids_subset = [re.sub('_.*','',x) for x in self.top10_ids]
			c_ids = Counter(ids_subset)
			if c_ids.most_common()[0][1] >1:
				data_in += 1
			else:
				dupes = False


		


	def results(self): 
		conn = boto.connect_s3(os.environ['access_key'], os.environ['access_secret_key'])
		bucket_name = os.environ['bucket_name']
		bucket = conn.get_bucket(bucket_name)

		img_data = []
		for x,val in enumerate(self.top10_ids):
			self.psql.execute(
			'''select name,gender,age,city,state,zip from data where id='%s';  
			''' % val)
			img_details = self.psql.fetchall()[0]
			key = val.encode('ascii','ignore')+'.jpg'
			#outfile = '/tmp/dogs/'+'m'+str(x)+'_'+key
			img = bucket.get_key(key)
			#img.get_contents_to_filename(outfile)
			outfile = img.generate_url(6000)
			img_data.append([val,outfile,self.top10_scores[x],img_details[0],img_details[1],img_details[2],img_details[3],img_details[4],img_details[5]])
		self.df = pd.DataFrame(np.array(img_data), columns=['id','img_loc','score','name','gender','age','city','state','zip'])
		self.df.to_csv('tmp/'+self.session_id+'.csv')







