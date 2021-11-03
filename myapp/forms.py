from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class TopCities(FlaskForm):
	cityName = StringField("City Name", validators=[DataRequired()])
	cityRank = IntegerField("City Rank", validators=[DataRequired()])
	isVisited = BooleanField("Visited")
	submit = SubmitField("Submit")
