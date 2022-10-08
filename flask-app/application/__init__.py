from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'bA5qzruPYLAyyx5QFNUVCg'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

print(app.config['SQLALCHEMY_DATABASE_URI'])
db =SQLAlchemy(app)

from application.routes import routes