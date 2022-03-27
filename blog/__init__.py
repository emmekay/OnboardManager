from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
#from elasticsearch import Elasticsearch
       

app = Flask(__name__)
app.config['SECRET_KEY'] = '877b4849e3ff6800714aeb090487807f77c78d7b5d26d13d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://c2101138:RedCatSaw1@csmysql.cs.cf.ac.uk:3306/c2101138_flasklabs'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

from blog import routes 

from flask_admin import Admin 
from blog.views import AdminView
from blog.models import User, Post, Comment 
admin = Admin(app, name='Admin panel', template_mode='bootstrap3')
admin.add_view(AdminView(User, db.session))
admin.add_view(AdminView(Post, db.session))
admin.add_view(AdminView(Comment, db.session))


#def create_app(config_class=Config):
 #   app = Flask(__name__)
  #  app.config.from_object(config_class)
#
 #   app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) if app.config['ELASTICSEARCH_URL'] else None 