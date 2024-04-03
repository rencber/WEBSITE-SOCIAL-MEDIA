from flask import Flask , render_template # imported Flask from flask package
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__) # this variable is build-in variable we can fall any python fall
## referring the main python file we are working with
## Flask want to get this parameter
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'

db = SQLAlchemy(app)





app.app_context().push()

from market import routes

