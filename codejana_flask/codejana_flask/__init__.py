from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)


app.config['SECRET_KEY']='thisisCSIT314App'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database/theDataBase.db'
# delete database that you had originally
# app.config['SQLALCHEMY_DATABASE_URI']='postgresql://username:password@hostname:port/databasename'

db=SQLAlchemy(app)
from codejana_flask import routes

# One2345siz!