import boto
import requesocks
import shutil
from pymongo import MongoClient
import os

def downloadNewImages(bucket, new_dog_img_dict, d_id):
	try:
		dfile = new_dog_img_dict[d_id]
		fname= d_id +'.jpg'
		if not bucket.get_key(fname):
			session = requesocks.session()
			session.proxies = {'http': 'socks5://127.0.0.1:9050','https': 'socks5://127.0.0.1:9050'}
	
			file_object = bucket.new_key(fname)
			r = session.get(dfile)
			if r.status_code == 200:
				with open(fname, 'wb') as f:
					r.raw.decode_content = True
					shutil.copyfileobj(r.raw, f)
				file_object.set_contents_from_filename('./'+fname,policy='public-read')
				os.remove(fname)
			else:
				client = MongoClient()
				db = client.pet
				err_coll = db.errs
				err_coll.insert_one({'id':record['id'], 'err':r.status_code})
	except:
		client = MongoClient()
		db = client.pet
		err_coll = db.errs
		e = sys.exc_info()[1]
		err_coll.insert_one({'id':record['id'], 'err':str(e)})