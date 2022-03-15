


from flask import Flask, jsonify, request
# from geoalchemy2 import Geometry

from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
db = SQLAlchemy(app)
uri=os.getenv("DB_URI")
key=os.getenv("S_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = uri

app.config['SECRET_KEY'] = key

from apps.post.models import post_info
from apps.post.depends import create_post
from apps.post.depends import get_post
from apps.weather.depends import get_weather


@app.route('/')
def hello():
    return "Hello World!"