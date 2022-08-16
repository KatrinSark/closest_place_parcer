import os
import re

import requests
from haversine import haversine as hs


# Выдает координаты по адресу
def address_to_geo(adrs) -> tuple:
    address_responce = requests.get(url=f"{os.getenv('GEOPARSER')}{adrs}")
    if address_responce.ok == False:
        return "0,0"
    else:
        position = address_responce.json()
        return f"{position['latitude']}, {position['longitude']}"


# возвращает подходящие по расстоянию координаты
def distance_parser(user_lon, user_lat, place_geo) -> str:
    user_geo = (user_lon, user_lat)
    if len(place_geo.split(",")) == 2:
        correct_geo = (
            float(place_geo.split(",")[1].replace(")", "")),
            float(place_geo.split(",")[0].replace("(", ""))
        )
    else:
        correct_geo = (0, 0)
    distance_in_km = (round(hs(user_geo, correct_geo), 2))
    if distance_in_km <= 3:
        check_list = re.findall(r'[^\S\n\t]+', place_geo)
        if len(check_list) != 0:
            return f"{correct_geo[1]}, {correct_geo[0]}"
        else:
            return f"{correct_geo[1]},{correct_geo[0]}"


# возвращает список ближайших координат всех нужных мест
def place_parser(model, user_lat, user_lon, db):
    # список координат всех нужных мест
    place_coords = [r.coords for r in db.session.query(model.coords)]
    # список ближайших координат всех нужных мест
    detected_coords_list = [distance_parser(float(user_lat), float(user_lon), i) for i in place_coords]
    return detected_coords_list
