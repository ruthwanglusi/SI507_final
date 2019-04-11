from flask import *
from flask_sqlalchemy import SQLAlchemy

##### Application Configuration #####
# reference https://github.com/SI508-F18/Songs-App-Class-Example/blob/master/main_app.py
app = Flask(__name__)
app.debug = True
app.use_reloader = True

app.config['SECRET_KEY'] = '7alsk8sgij9ury456skg12qjh3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./park_info.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Set up Flask debug stuff
db = SQLAlchemy(app) # For database use
session = db.session # to make queries easy

##### Set Up Models #####
class State(db.Model):
    __tablename__ = 'STATE'
    state_id = db.Column(db.Integer, primary_key=True)
    stateName = db.Column(db.String(120),unique=True, nullable=False)

    def __repr__(self):
        return '{}'.format(self.name)

class Type(db.Model):
    __tablename__ = 'PARK TYPE'
    type_id = db.Column(db.Integer, primary_key=True)
    typeName = db.Column(db.String(240),unique=True, nullable=False)

    def __repr__(self):
        return '{}'.format(self.name)

class Park(db.Model):
    __tablename__ = 'PARK'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(240), nullable=False)
    descrip = db.Column(db.String)

    state_id = db.Column(db.Integer, db.ForeignKey('STATE.id'))
    state = db.relationship('State', backref='inState', lazy=True)

    type_id = db.Column(db.Integer, db.ForeignKey('PARK TYPE.id'))
    type = db.relationship('Type',backref='isType', lazy=True)

    def __repr__(self):
        return '{} || {} | {}'.format(self.name, self.stateName, self.parkType)


##### Run the Program #####
if __name__ == '__main__':
    # db.drop_all()
    db.create_all() # This will create database in current directory
    # app.run()
