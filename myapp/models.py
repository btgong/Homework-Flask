from myapp import db

class Cities(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	cityName=db.Column(db.String(64), index=True)
	cityRank=db.Column(db.Integer)
	isVisited=db.Column(db.Boolean)
