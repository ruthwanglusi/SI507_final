import os
from flask import *
from flask_sqlalchemy import SQLAlchemy
from SI507project_tool_pop import *
from SI507project_tool_scrape import *

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
#Set up association Table between artists and albums
Park_State = db.Table('PARK_STATE',
    db.Column('park_id', db.Integer, db.ForeignKey('PARK.park_id'), primary_key=True),
    db.Column('state_id', db.Integer, db.ForeignKey('STATE.id'), primary_key=True)
)

class Park(db.Model):
    __tablename__ = 'PARK'
    park_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(240), nullable=False)
    descrip = db.Column(db.String)

    # TYPE & PARK (1-many)
    type_id = db.Column(db.Integer, db.ForeignKey('TYPE.id'))
    type = db.relationship('Type', backref='type', lazy=True)

    # STATE & PARK (many-many)
    # state_id = db.Column(db.Integer, db.ForeignKey('PARK_STATE.state_id'))
    states = db.relationship('State', secondary = Park_State, lazy='subquery',
    backref=db.backref('states',lazy=True))

    def __repr__(self):
        # ***********'query the type table = my name'
        return f'{self.name}\n{self.type}\n{self.states}\n{self.descrip}'

# TYPE & PARK (1-many)
class Type(db.Model):
    __tablename__ = 'TYPE'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250),unique=True, nullable=False)

    def __repr__(self):
        return f'This is a {self.name}.'

# STATE & PARK (many-many)
class State(db.Model):
    __tablename__ = 'STATE'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120),unique=True, nullable=False)

    def __repr__(self):
        return f'{self.name}'

##### Routes #####
@app.route('/')
def home():
    return 'MAPPPP'


##### Run the Program #####
if __name__ == '__main__':
    # db.drop_all()
    db.create_all()
    parks = set_db_data()
    print(parks)


    app.run()

# References:
# https://github.com/si507-w19/database_population_flask_example/blob/master/app.py
