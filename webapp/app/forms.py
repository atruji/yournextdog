from flask.ext.wtf import Form
from wtforms import StringField, RadioField, IntegerField, FileField
from wtforms import validators

class SearchForm(Form):
    dogurl = StringField('dogurl',validators=[validators.URL(require_tld=True, message="Invalid URL")])
    zipcode = IntegerField('zipcode', validators=[validators.DataRequired(message='Zipcode required!')])
    radius = RadioField('radius', choices=[('value','100 Miles'),('value_two','500 Miles')], validators=[validators.Required(message="Search radius required!")])
