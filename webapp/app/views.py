from flask import render_template, flash, redirect,url_for, request
from app import app
from .forms import SearchFormWeb, SearchFormFile
import pandas as pd
import re
import random
from matchengine.DoggyMatchEngine import DoggyMatchEngine
import os
from werkzeug import secure_filename 


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def search():
	formfile = SearchFormFile()
	formweb = SearchFormWeb()
	return render_template('index__op__image_full_screen.html', 
                           title='Search',
                           formfile=formfile,
                           formweb=formweb)
