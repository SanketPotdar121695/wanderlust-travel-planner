import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)

DATABASE_URL = os.environ.get('db_url')
secret_key = os.environ.get('SECRET_KEY')

# Configure SQLite database
app.config['SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

from myapp.routes import destinations_routes, expenses_routes, itineraries_routes, other_routes