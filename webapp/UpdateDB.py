from pymongo import MongoClient
from pymongo import errors
import requests
import numpy as np
import os
import boto
import pandas as pd
import psycopg2
import json

class NightlyUpdate(object):
	def __init__(self):
		self.client = MongoClient()
		self.db = self.client.pet
		self.shelter_coll = self.db.shelter
		self.dogs_coll = self.db.dog
		self.err_coll = self.db.errs
		#self.conn = psycopg2.connect(dbname='dogs', user='ubuntu')
		#self.psql = self.conn.cursor()
		self.states=['AL','AK','AZ','AR','CA','CO','CT','DE','DC','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','PR','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY',]
		self.botoconn = boto.connect_s3(os.environ['access_key'], os.environ['access_secret_key'])
		bucket_name = os.environ['bucket_name']
		self.bucket = self.botoconn.get_bucket(bucket_name)
		#self.socks_port = 9050
		#self.tor_process = stem.process.launch_tor_with_config(config = {'SocksPort': str(self.socks_port)})

		
	def updateShelters(self):   
		def insert_shelter(shelter, collection):
			if not collection.find_one({"id" : {'t': shelter['id']['t']}}):
				try:
					print "Inserting shelter " + str(shelter['name']['t'].encode('ascii','ignore'))
					collection.insert_one(shelter)
				except:
					pass

		def get_state_shelters(state):
			unfilled = True
			while unfilled:
				z1 = requests.get('http://api.petfinder.com/shelter.find?key=7d43f07af007bb1dc8c1bdb73508271e&location='+state+'&output=full&format=json&count=1000')
				if z1.status_code==200:
					unfilled = False
			unfilled = True
			while unfilled:
				z2 = requests.get('http://api.petfinder.com/shelter.find?key=7d43f07af007bb1dc8c1bdb73508271e&location='+state+'&output=full&format=json&count=1000&offset=1000')
				if z2.status_code==200:
					unfilled = False
			res1 = z1.content.replace('$','')
			res2 = z2.content.replace('$','')
			jres1 = json.loads(res1)
			jres2 = json.loads(res2)
			shelters1 = jres1['petfinder']['shelters']['shelter']
			shelters2 = jres2['petfinder']['shelters']['shelter']
			allshelters = shelters1 + shelters2
			return allshelters

		for x in self.states:
			shelters = get_state_shelters(x)
			for i in shelters:
				insert_shelter(i,self.shelter_coll)

	def updateDogRecs(self):
		def insert_dog(dog, collection):
			if not collection.find_one({"id" : {'t': dog['id']['t']}}):
				try:
					collection.insert_one(dog)
				except:
					pass
		def get_dogs_by_shelter(shelter, tally):
			if tally < 5604:
				z1 = requests.get('http://api.petfinder.com/shelter.getPets?key=7d43f07af007bb1dc8c1bdb73508271e&id='+shelter+'&output=full&format=json&count=1000')
			else:
				z1 = requests.get('http://api.petfinder.com/shelter.getPets?key=26f1671619da6ad88c07df6628f24cdd&id='+shelter+'&output=full&format=json&count=1000')
			if z1.status_code !=200:
				
			res1 = z1.content.replace('$','')
			jres1 = json.loads(res1)
			tally+=1
			if not jres1['petfinder']['pets']:
				return None,None
			if len(jres1['petfinder']['pets']['pet']) < 1000:
				allpets = jres1['petfinder']['pets']['pet']
			else:
				if tally <5604:
					z2 = requests.get('http://api.petfinder.com/shelter.getPets?key=7d43f07af007bb1dc8c1bdb73508271e&id='+shelter+'&output=full&format=json&count=1000&offset=1000')
				else:
					z2 = requests.get('http://api.petfinder.com/shelter.getPets?key=26f1671619da6ad88c07df6628f24cdd&id='+shelter+'&output=full&format=json&count=1000&offset=1000')
				res2 = z2.content.replace('$','')
				jres2 = json.loads(res2)
				tally+=1
			
				if not jres2['petfinder']['pets']:
					allpets = jres1['petfinder']['pets']['pet']
				else: 
					allpets = jres1['petfinder']['pets']['pet'] + jres2['petfinder']['pets']['pet']
				
			dogs = []
			if type(allpets)==dict:
				allpets = [allpets]
			for x in xrange(len(allpets)):
				if allpets[x]['animal']['t']=='Dog':
					dogs.append(allpets[x])
			return dogs, tally

		shelter_lst=[]
		for shelter in self.shelter_coll.find():
			shelter_lst.append(shelter['id']['t'])
		errs = []
		tally = 0
		for x,shelter in enumerate(shelter_lst):
			try:
				dogs, tally = get_dogs_by_shelter(shelter,tally)
				
			except (ValueError,KeyError):
				errs.append(shelter)
				continue 
			if dogs is not None: 
				for dog in dogs: 
					insert_dog(dog, self.dogs_coll)
				if not x % 100: 
					print '%s percent of shelters complete.' % (str(100*(x/float(len(shelter_lst)))))
		pd.Series(errs).to_csv('errs.csv',index=False)

	def updateDogImgLst(self):
		def getCurImgLst():
			self.dog_img_dict = {}
			d_id = coll.find_one()['id']['t']
			for i,x in enumerate(coll.find_one()['media']['photos']['photo']):
				if x['@size']=='pn' or x['@size']=='x':
					dog_img_dict[str(d_id)+'_'+str(i)] = x['t']
			self.dog_img_lst = self.dog_img_dict.keys()
		def crossRefSQL(self):
			self.psql.execute('select id from records;')
			sql_lst = [x[0] for x in self.psql.fetchall()]
			new_dog_imgs = []
			for x in self.dog_img_lst:
				if x not in sql_lst:
					new_dog_imgs.append(x)
			outdated_dog_imgs = []
			for x in sql_lst:
				if x not in self.dog_img_lst:
					outdated_dog_imgs.append(x)
			for x in outdated_dog_imgs:
				self.psql.execute('''delete from records where id='%s';''' % x)
				self.conn.commit()
				#key = x.encode('ascii','ignore')+'.jpg'    
				#self.bucket.delete_key(key)
			self.new_dog_img_dict =[]
			for x in new_dog_imgs:
				self.new_dog_img_dict[x] = self.dog_img_dict[x]
		def downloadNewImages():
			self.success = []
			for x in self.new_dog_img_dict.keys():
				try:
					dfile = new_dog_img_dict[x]
					fname= x +'.jpg'
					if not self.bucket.get_key(fname):
						session = requesocks.session()
						session.proxies = {'http': 'socks5://127.0.0.1:9050','https': 'socks5://127.0.0.1:9050'}
				
						file_object = self.bucket.new_key(fname)
						r = session.get(dfile)
						if r.status_code == 200:
							with open(fname, 'wb') as f:
								r.raw.decode_content = True
								shutil.copyfileobj(r.raw, f)
							file_object.set_contents_from_filename('./'+fname,policy='public-read')
							self.success.append(x)
							os.remove(fname)
							#time.sleep(1)
						else:
							self.err_coll.insert_one({'id':record['id'], 'err':r.status_code})
				except:
					e = sys.exc_info()[1]
					self.err_coll.insert_one({'id':record['id'], 'err':str(e)})













