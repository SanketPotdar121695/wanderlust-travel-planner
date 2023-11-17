import os
from myapp import app
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

DATABASE_URL = os.environ.get('db_url')
secret_key = os.environ.get('SECRET_KEY')

# Configure SQLite database
app.config['SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

db = SQLAlchemy(app)