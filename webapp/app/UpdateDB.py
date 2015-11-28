from pymongo import MongoClient
from pymongo import errors
import requests
import numpy as np
import os
import boto
import pandas as pd
import psycopg2

class NightlyUpdate(object):
    def __init__(self):
        self.client = MongoClient()
        self.db = client.pet
        self.shelter_coll = db.shelter
        self.dogs_coll = db.dog
        self.err_coll = db.errs
        self.conn = psycopg2.connect(dbname='dogs', user='ubuntu')
        self.psql = self.conn.cursor()
        self.states=['AL','AK','AZ','AR','CA','CO','CT','DE','DC','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','PR','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY',]
        self.botoconn = boto.connect_s3(os.environ['access_key'], os.environ['access_secret_key'])
        bucket_name = os.environ['bucket_name']
        self.bucket = conn.get_bucket(bucket_name)
        #self.socks_port = 9050
        #self.tor_process = stem.process.launch_tor_with_config(config = {'SocksPort': str(self.socks_port)})

        
    def updateShelters(self):   
        def insert_shelter(shelter, collection):
            if not collection.find_one({"id" : {'t': shelter['id']['t']}}):
                try:
                    print "Inserting shelter " + str(shelter['name']['t'].encode('ascii','ignore'))
                    collection.insert_one(shelter)
                except errors.DuplicateKeyError:
                    print "Duplicates"

        def get_state_shelters(state):
            z1 = requests.get('http://api.petfinder.com/shelter.find?key=7d43f07af007bb1dc8c1bdb73508271e&location='+state+'&output=full&format=json&count=1000')
            z2 = requests.get('http://api.petfinder.com/shelter.find?key=7d43f07af007bb1dc8c1bdb73508271e&location='+state+'&output=full&format=json&count=1000&offset=1000')
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
                insert_shelter(i,coll)

    def updateDogRecs(self):

        def get_dogs_by_shelter(shelter):
            z1 = requests.get('http://api.petfinder.com/shelter.getPets?key=26f1671619da6ad88c07df6628f24cdd&id='+shelter+'&output=full&format=json&count=1000')
            res1 = z1.content.replace('$','')
            jres1 = json.loads(res1)
            num_requests = 1
            if not jres1['petfinder']['pets']:
                return None,None
            if len(jres1['petfinder']['pets']['pet']) < 1000:
                allpets = jres1['petfinder']['pets']['pet']
            else:
                z2 = requests.get('http://api.petfinder.com/shelter.getPets?key=26f1671619da6ad88c07df6628f24cdd&id='+shelter+'&output=full&format=json&count=1000&offset=1000')
                res2 = z2.content.replace('$','')
                jres2 = json.loads(res2)
                num_requests = 2
            
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
            return dogs, num_requests

        def insert_dog(dog, collection):
            if not collection.find_one({"id" : {'t': dog['id']['t']}}):
                try:
                    collection.insert_one(dog)
        
        shelter_lst=[]
        for shelter in self.shelter_coll.find():
            shelter_lst.append(shelter['id']['t'])
        errs = []
        total_reqs = 0
        for x,shelter in enumerate(shelter_lst):
            try:
                dogs, num_requests = get_dogs_by_shelter(shelter)
                
            except (ValueError,KeyError):
                errs.append(shelter)
                continue 
            if dogs is not None: 
                total_reqs += num_requests
                for dog in dogs: 
                    insert_dog(dog, coll)
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
            new_dog_imgs = [x if x not in sql_lst for x in self.dog_img_lst]
            outdated_dog_imgs = [x if x not in self.dog_img_lst for x in sql_lst]
            for x in outdated_dog_imgs:
                self.psql.execute('delete from records where id='%s'', x)
                self.conn.commit()
                #key = x.encode('ascii','ignore')+'.jpg'    
                #self.bucket.delete_key(key)
            self.new_dog_img_dict =[]
            for x in new_dog_imgs:
                self.new_dog_img_dict[x] = self.dog_img_dict[x]
        def downloadNewImages:
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













