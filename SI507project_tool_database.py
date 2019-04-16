from flask import *
from flask_sqlalchemy import SQLAlchemy

##### Application Configuration #####
# reference https://github.com/SI508-F18/Songs-App-Class-Example/blob/master/main_app.py
app = Flask(__name__)
app.debug = True
app.use_reloader = True
#
# app.config['SECRET_KEY'] = '7alsk8sgijiuskfl3987sgkg12qjh3'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./park_info.db'
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# # Set up Flask debug stuff
# db = SQLAlchemy(app) # For database use
# session = db.session # to make queries easy

##### Set Up Models #####
# class State(db.Model):
#     __tablename__ = 'STATE'
#     state_id = db.Column(db.Integer, primary_key=True)
#     stateName = db.Column(db.String(120),unique=True, nullable=False)
#     parks = db.relationship('Park', secondary = 'PARK_STATE', backref='hasParks', lazy=True)
#
#     def __repr__(self):
#         return '{}'.format(self.name)
#
# class Type(db.Model):
#     __tablename__ = 'TYPE'
#     id = db.Column(db.Integer, primary_key=True)
#     typeName = db.Column(db.String(240),unique=True, nullable=False)
#
#     def __repr__(self):
#         return '{}'.format(self.name)
#
# class Park(db.Model):
#     __tablename__ = 'PARK'
#     park_id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(240), nullable=False)
#     descrip = db.Column(db.String)
#
#     state_id = db.Column(db.Integer, db.ForeignKey('STATE.state_id'))
#     states = db.relationship('State', secondary = 'PARK_STATE', backref='inStates', lazy=True)
#
#     type_id = db.Column(db.Integer, db.ForeignKey('TYPE.id'))
#     type = db.relationship('Type', backref='isType', lazy=True)
#
#     def __repr__(self):
#         return '{} || {} | {}'.format(self.name, self.stateName, self.parkType)
#
# class Park_State(db.Model):
# 	__tablename__ = 'PARK_STATE'
# 	state_id = db.Column(db.Integer, db.ForeignKey('STATE.state_id'), primary_key = True)
# 	park_id = db.Column(db.Integer, db.ForeignKey('PARK.park_id'), primary_key = True)

##### Routes #####
@app.route('/')
def home():
    return '<h1>National Parks in the US</h1>'

##### Run the Program #####
if __name__ == '__main__':
    # db.drop_all()
    # db.create_all() # This will create database in current directory
    app.run()

    # ##### Read the CSV File #####
    # data = []
    # with open('park_scrape.csv') as csv_file:
    #     csv_reader = csv.reader(csv_file)
    #     next(csv_reader)
    #
    #     for row in csv_reader:
    #         data.append(row)
    #
    # # try:
    #
    # for i in data:
    #     """info = Park(**{
    #     'name' : i[0],
    #     'descrip' : i[2],
    #     'states' : i[4],
    #     'type' : i[1]
    #     })"""
    #     park = Park(**{
    #     'name' : i[0],
    #     'descrip' : i[2],
    #     })
    #     s = State()
    #     park.states.append(s)
    #     park.types.
    #     session.add(info)
    # session.commit()
    # # except:
    # #     session.rollback()
    # # finally:
    # session.close()


# References:
# https://stackoverflow.com/questions/31394998/using-sqlalchemy-to-load-csv-file-into-a-database
