from flask import render_template, flash, redirect,url_for, request
from app import app
from .forms import SearchFormWeb, SearchFormFile
import pandas as pd
import re
import random
from matchengine.DoggyMatchEngine import DoggyMatchEngine
import os
from werkzeug import secure_filename 
import threading

UPLOAD_FOLDER = 'app/static/uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'JPEG', 'JPG'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def form_validate(formfile,formweb):
	if formfile.is_submitted():
		submitted=True
		if formfile.zipcode.data and formfile.radius.data and formfile.fileName.data:
			return True, True, 'SearchFormFile'
		else:
			return True, False, 'Please fill out all forms!'
	elif formweb.is_submitted():
		if formweb.zipcode.data and formweb.radius.data and formweb.dogurl.data:
			return True, True,'SearchFormWeb'
		else:
			return True, False, 'Please fill out all forms!'
	else:
		return False, float('NaN'), float('NaN')

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def search():
	err=''
	switch_sect = 'false'
	formfile = SearchFormFile()
	formweb = SearchFormWeb()

	submitted, valid, ftype = form_validate(formfile,formweb)
	if valid and ftype=='SearchFormFile':
		searchtype='file'
		filename = secure_filename(formfile.fileName.data.filename)
		if filename and allowed_file(filename): 
			file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
			formfile.fileName.data.save(file_path)
			user_file = file_path
		else:
			return redirect('/')
		session_id = str(random.randint(1,999999))
		user_zip = formfile.zipcode.data
		if formfile.radius.data == 'value':
			radius = 100
		else:
			radius = 500
		return redirect(url_for('get_results',sess_id=session_id,zipcode=user_zip,img=user_file,radius=radius))
	
	elif valid and ftype=='SearchFormWeb':
		searchtype='web'
		user_file = formweb.dogurl.data
		session_id = str(random.randint(1,999999))
		user_zip = formweb.zipcode.data
		if formweb.radius.data == 'value':
			radius = 100
		else:
			radius = 500
		return redirect(url_for('get_results',sess_id=session_id,zipcode=user_zip,img=user_file,radius=radius, searchtype=searchtype))
	if not valid:
		switch_sect = 'true'
		err = ftype
	return render_template('index__op__image_full_screen.html',id='services', 
                           title='Search',
                           formfile=formfile,
                           formweb=formweb,
                           err=err,
                           switcher=switch_sect)


@app.route('/results', methods=['GET','POST'])
def get_results():
	session_id = request.args.get('sess_id')
	user_zip = request.args.get('zipcode')
	dog_url = request.args.get('img')
	user_radius = request.args.get('radius')
	matcher = DoggyMatchEngine(GPU=False)
	t = threading.Thread(name='child procs', target=matcher.fit, args=(dog_url,session_id))
	t.start()
	matcher.sql_import(user_zip,user_radius)
	t.join()
	matcher.match()
	matcher.results()

	if request.args.get('searchtype')=='web':
		user_file = matcher.orig_file.replace('app/','../')
	else: 
		user_file = dog_url.replace('app/','../')
	df = matcher.df
	images = df['img_loc'].values
	names = df['name'].values
	genders = df['gender'].values
	ages = df['age'].values
	match_scores = (1 - df['score'].values.astype(float))*100
	match_scores = [round(x,2) for x in match_scores]
	ids = df['id'].values
	ids = [re.sub('_.*','',x) for x in ids]
	profile_pages = ["https://www.petfinder.com/petdetail/"+x for x in ids]

	data = zip(images,names,genders,ages,match_scores,profile_pages)
	return render_template('results.html', data=data, user_img=user_file)

    
