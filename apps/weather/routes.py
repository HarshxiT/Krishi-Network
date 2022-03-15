from flask import Blueprint
from apps.weather.controller import getWeather



weather_bp = Blueprint('weather_bp', __name__)
weather_bp.route('/getWeather', methods=['GET'])(getWeather)