from flask import request
from flask import jsonify
from flask import Blueprint
import re

from sqlalchemy import or_
from sqlalchemy.sql.operators import op

from main.extensions import db
from main.models import models
from main.help_methods import place_parser

api = Blueprint('api', __name__)


# Запрос по координатам
@api.route('/place_parser', methods=['GET'])
def geodatas():
    user_geodata = request.args.get('geodata')
    place = request.args.get('place')
    model = models[f"{place}"]

    lon = (re.findall(r'\w+.\w+$', user_geodata))[0]
    lat = (re.findall(r'^\w+.\w+', user_geodata))[0]

    # возвращает список ближайших координат всех нужных мест
    detected_coords_list = place_parser(model, lat, lon, db)
    info = db.session.query(model).filter(model.coords.in_(detected_coords_list)).all()
    return jsonify(info)


# Запрос на ближайшие точки с корюшкой
@api.route('/fish_spots', methods=['GET'])
def fish_spots():
    user_geodata = request.args.get('geodata')
    model = models["fish_spot"]
    try:
        lat = (re.findall(r'\w+.\w+$', user_geodata))[0]
        lon = (re.findall(r'^\w+.\w+', user_geodata))[0]

        # возвращает список ближайших координат всех нужных мест
        detected_coords_list = place_parser(model, lat, lon, db)

        info = db.session.query(model) \
            .filter(model.coords.in_(detected_coords_list)) \
            .all()
        data = {'data': info}
        return jsonify(data)

    except IndexError or TypeError:
        error_data = {'data': 'Произошла ошибка. Попробуйте еще раз.'}
        return jsonify(error_data)
