from myapp import myapp_obj, db
from flask import render_template, flash, redirect
from myapp.forms import TopCities
from myapp.models import Cities

@myapp_obj.route("/", methods=['GET', 'POST'])
def home():
	form = TopCities()
	title = 'Top Cities'
	name = 'Brandon'

	if form.validate_on_submit():
		city = Cities(cityName = form.cityName.data, cityRank = form.cityRank.data, isVisited = form.isVisited.data)
		db.session.add(city)
		db.session.commit()
		flash(f'Added {city.cityName} to database')
		return redirect('/')

	top_cities = Cities.query.order_by(Cities.cityRank).all()

	return render_template('home.html', title = title, name = name, top_cities = top_cities, form = form)

