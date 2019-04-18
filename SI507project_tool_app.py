import os
from flask import *
from flask_sqlalchemy import SQLAlchemy
from SI507project_tool_db import *

##### Application Configuration #####
app = Flask(__name__)
app.debug = True
app.use_reloader = True

app.config['SECRET_KEY'] = '7alsk8sgijiuskfl3987sgkg12qjh3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./park_info.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Set up Flask debug stuff
db = SQLAlchemy(app) # For database use
session = db.session # to make queries easy


##### Set Up Models #####

class Park(db.Model):
    __tablename__ = 'PARK'
    park_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(240), nullable=False)
    descrip = db.Column(db.String)

    # TYPE & PARK (1-many)
    type_id = db.Column(db.Integer, db.ForeignKey('TYPE.id'))
    type = db.relationship('Type', backref='isType', lazy=True)

    # STATE & PARK (many-many)
    state_id = db.Column(db.Integer, db.ForeignKey('STATE.id'))
    states = db.relationship('State', secondary = 'PARK_STATE', backref='inStates', lazy=True)

    def __repr__(self):
        return '{} || {} | {}'.format(self.name, self.stateName, self.parkType)

# TYPE & PARK (1-many)
class Type(db.Model):
    __tablename__ = 'TYPE'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250),unique=True, nullable=False)

    def __repr__(self):
        return f'This is a {self.name} park'

# STATE & PARK (many-many)
class Park_State(db.Model):
	__tablename__ = 'PARK_STATE'
	state_id = db.Column(db.Integer, db.ForeignKey('STATE.id'), primary_key = True)
	park_id = db.Column(db.Integer, db.ForeignKey('PARK.park_id'), primary_key = True)

class State(db.Model):
    __tablename__ = 'STATE'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120),unique=True, nullable=False)
    parks = db.relationship('Park', secondary = 'PARK_STATE', backref='state', lazy=True)

    def __repr__(self):
        return '{}'.format(self.name)

##### Routes #####
@app.route('/')
def home():
    pass

##### Run the Program #####
if __name__ == '__main__':
    # db.drop_all()
    db.create_all()
    app.run()



# References:
# https://github.com/si507-w19/database_population_flask_example/blob/master/app.py
