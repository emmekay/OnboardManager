from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager       

app = Flask(__name__)
app.config['SECRET_KEY'] = '877b4849e3ff6800714aeb090487807f77c78d7b5d26d13d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://c2101138:LearnFlask2day@csmysql.cs.cf.ac.uk:3306/c2101138_flasklabs'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

from blog import routes 