from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

import dotenv

# import dotenv
dotenv.load_dotenv()

db = SQLAlchemy()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

db.init_app(app)


class SupaUser(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  email = db.Column(db.String(100), nullable=False)
  password = db.Column(db.String(100), nullable=False)


with app.app_context():
  db.create_all()
