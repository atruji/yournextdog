from flask.ext.wtf import Form
from wtforms import StringField, RadioField, IntegerField, FileField
from wtforms import validators

class SearchFormWeb(Form):
    dogurl = StringField('dogurl')
    zipcode = IntegerField('zipcode')
    radius = RadioField('radius', choices=[('value','100 Miles'),('value_two','500 Miles')])

class SearchFormFile(Form):
    fileName = FileField()
    zipcode = IntegerField('zipcode')
    radius = RadioField('radius', choices=[('value','100 Miles'),('value_two','500 Miles')])