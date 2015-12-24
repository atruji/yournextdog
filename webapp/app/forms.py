from flask.ext.wtf import Form
from wtforms import StringField, RadioField, IntegerField, FileField
from wtforms.validators import InputRequired

class SearchFormWeb(Form):
    dogurl = StringField('dogurl', validators=[InputRequired()])
    zipcode = IntegerField('zipcode', validators=[InputRequired()])
    radius = RadioField('radius', choices=[('value','100 Miles'),('value_two','500 Miles')], validators=[InputRequired()])

class SearchFormFile(Form):
    fileName = FileField(validators=[InputRequired()])
    zipcode = IntegerField('zipcode', validators=[InputRequired()])
    radius = RadioField('radius', choices=[('value','100 Miles'),('value_two','500 Miles')], validators=[InputRequired()])