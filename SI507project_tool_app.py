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

'''
Set Up Database
'''
#STATE & PARK association table
Park_State = db.Table('PARK_STATE',
    db.Column('park_id', db.Integer, db.ForeignKey('PARK.park_id')),
    db.Column('state_id', db.Integer, db.ForeignKey('STATE.id'))
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

    # def __repr__(self):
    #     return f'{self.name}\n{self.type}\n{self.states}\n{self.descrip}'

# TYPE & PARK (1-many)
class Type(db.Model):
    __tablename__ = 'TYPE'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250),unique=True) #some park may not have a type

    def __repr__(self):
        return f'This is a {self.name}.'

# STATE & PARK (many-many)
class State(db.Model):
    __tablename__ = 'STATE'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120),unique=True, nullable=False)

    def __repr__(self):
        return f'{self.name}'

'''
Set Up Routes
'''
@app.route('/')
def home():
    num = 13
    return render_template('main.html', total=num)
    #total is a variable in main.html
    

@app.route('/state')
def type():
    return 'state page'

@app.route('/type')
def state():
    return 'type page'


'''
Run the Program
'''
#create a new park_info.db
def create_db():
    # db.drop_all()
    db.create_all()

    coll = parse_parks()
    namesAll = coll[0]
    typesAll = coll[1]
    desAll = coll[2]
    statesAll = coll[3]

    # count = 0

    for i in range(len(namesAll)):

        name = coll[0][i]
        type = coll[1][i]
        descrip = coll[2][i]
        states = coll[3][i]

        # if len(type) == 0:
        #     count += 1
        # else:
        #     pass

        new_park(name,descrip,type,states)
    # print(count)

if __name__ == '__main__':
    # create_db()
    app.run()

# References:
# https://github.com/si507-w19/database_population_flask_example/blob/master/app.py
# Using Jinja2 Templates in Flask https://www.youtube.com/watch?v=exR1kxpd1cY
#???why missing 200 parks? empty list for states 8, none for type 42
