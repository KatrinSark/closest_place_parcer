import os

import requests
from io import BytesIO, TextIOWrapper
from main.models import models
from main.extensions import db
from main.help_methods import address_to_geo
from zipfile import ZipFile
import csv
from tqdm import tqdm


def download_zip_to_dict(url):
    r = requests.get(url, stream=True)
    zip_file = ZipFile(BytesIO(r.content))

    with zip_file.open(zip_file.namelist()[0], 'r') as infile:
        reader = csv.reader(TextIOWrapper(infile, 'utf-8'))
        for row in reader:
            # process the CSV here
            yield row


def update_database(**kwargs):
    for row in tqdm(download_zip_to_dict(kwargs["sport_url"]), desc="Sport"):
        if 'Адрес' not in row:
            parsed = address_to_geo(row[3])
            sport = models["sport"](
                name=row[1],
                type=row[2],
                address=row[3],
                address_info=row[4],
                coords=parsed,
                subway=row[6],
                district=row[7],
                phone=row[8],
                website=row[9],
                status=row[10],
                working_hour=row[11],
                notes=row[12],
                inventory=row[13],
                instructor=row[14],
                dressing_room=row[15],
                baggage_room=row[16],
                other=row[17]
            )
            db.session.add(sport)
            db.session.commit()
    for row in tqdm(download_zip_to_dict(kwargs["pass_table_url"]), desc="Pass"):
        if 'Адрес' not in row:
            parsed = address_to_geo(row[3])
            pass_table = models["passtable"](
                number=row[0],
                name=row[1],
                division_number=row[2],
                address=row[3],
                phone=row[4],
                working_hours=row[5],
                coords=parsed
            )
            db.session.add(pass_table)
            db.session.commit()
    print("+")
    for row in tqdm(download_zip_to_dict(kwargs["school_url"]), desc="School"):
        if 'Адрес' not in row:
            parsed = address_to_geo(row[3])
            school = models["school"](
                district=row[0],
                name=row[1],
                short_name=row[2],
                address=row[3],
                leader=row[4],
                phone=row[5],
                fax=row[6],
                mail=row[7],
                municipal=row[8],
                INN=row[9],
                OGRN=row[10],
                notes=row[11],
                coords=parsed
            )
            db.session.add(school)
            db.session.commit()
    for row in tqdm(download_zip_to_dict(kwargs["kindergarden_url"]), desc="Kindergarten"):
        if 'Адрес' not in row:
            parsed = address_to_geo(row[3])
            kindergarden = models["kindergarden"](
                district=row[0],
                name=row[1],
                short_name=row[2],
                address=row[3],
                leader=row[4],
                phone=row[5],
                nursery=row[6],
                fax=row[7],
                mail=row[8],
                municipal=row[9],
                INN=row[10],
                OGRN=row[11],
                notes=row[12],
                coords=parsed
            )
            db.session.add(kindergarden)
            db.session.commit()
    for row in tqdm(download_zip_to_dict(kwargs["vet_url"]), desc="Vet"):
        if 'Адрес' not in row:
            parsed = address_to_geo(row[2])
            vet = models["vet"](
                name=row[0],
                district=row[1],
                address=row[2],
                phone=row[3],
                number=row[4],
                notes=row[5],
                coords=parsed,
            )
            db.session.add(vet)
            db.session.commit()
    for row in tqdm(download_zip_to_dict(kwargs["clinic_url"]), desc="Clinic"):
        if 'Адрес' not in row:
            clinic = models["clinic"](
                number=row[0],
                name=row[1],
                type=row[2],
                address=row[3],
                coords=row[4],
                district=row[5],
                leader=row[6],
                phone=row[7],
                fax=row[8],
                working_hours=row[9],
            )
            db.session.add(clinic)
            db.session.commit()
    for row in tqdm(download_zip_to_dict(kwargs["exhibition_hall_url"]), desc="ExhibitionHall"):
        if 'Адрес' not in row:
            exhibition_hall = models["exhibition_hall"](
                number=row[0],
                name=row[1],
                name_eng=row[2],
                type=row[3],
                address=row[4],
                phone=row[5],
                website=row[6],
                mail=row[7],
                description_eng=row[9],
                description=row[8],
                notes=row[10],
                coords=row[11],
            )
            db.session.add(exhibition_hall)
            db.session.commit()
    for row in tqdm(download_zip_to_dict(kwargs["hotel_url"]), desc="Hotels"):
        if 'Адрес' not in row:
            hotel = models["hotels"](
                number=row[0],
                name=row[1],
                type=row[2],
                room=row[3],
                bedroom=row[4],
                address=row[5],
                district=row[6],
                phone=row[7],
                fax=row[8],
                website=row[9],
                mail=row[10],
                notes=row[11],
                services=row[12],
                coords=row[13]
            )
            db.session.add(hotel)
            db.session.commit()
    for row in tqdm(download_zip_to_dict(kwargs["sightseeing_url"]), desc="Sightseeing"):
        if 'Название' not in row:
            sightseeing = models["sightseeing"](
                number=row[0],
                type=row[1],
                name=row[2],
                short_name=row[3],
                name_eng=row[4],
                place_type=row[5],
                address=row[6],
                phone=row[7],
                website=row[8],
                mail=row[9],
                description_eng=row[10],
                description=row[11],
                history=row[12],
                history_eng=row[13],
                notes=row[14],
                working_hours=row[15],
                working_hours_eng=row[16],
                coords=row[17]
            )
            db.session.add(sightseeing)
            db.session.commit()
    for row in tqdm(download_zip_to_dict(kwargs["cinema_url"]), desc="Cinema"):
        if 'Адрес' not in row:
            cinema = models["cinema"](
                number=row[0],
                name=row[1],
                name_eng=row[2],
                address=row[3],
                district=row[4],
                phone=row[5],
                website=row[6],
                mail=row[7],
                notes=row[8],
                coords=row[9]
            )
            db.session.add(cinema)
            db.session.commit()
    for row in tqdm(download_zip_to_dict(kwargs["museum_url"]), desc="Museums"):
        if 'Адрес' not in row:
            museum = models["museums"](
                number=row[0],
                name=row[1],
                name_eng=row[2],
                type=row[3],
                county=row[4],
                address=row[5],
                district=row[6],
                phone=row[7],
                website=row[8],
                mail=row[9],
                description=row[10],
                description_eng=row[11],
                working_hours=row[12],
                notes=row[13],
                coords=row[14],
                INN=row[15],
                OGRN=row[16],
            )
            db.session.add(museum)
            db.session.commit()
    for row in tqdm(download_zip_to_dict(kwargs["restaurant_url"]), desc="Restaurants"):
        if 'Адрес' not in row:
            restaurant = models["restaurants"](
                number=row[0],
                name=row[1],
                name_eng=row[2],
                address=row[3],
                phone=row[4],
                website=row[5],
                mail=row[6],
                kitchen=row[7],
                notes=row[8],
                coords=row[9]
            )
            db.session.add(restaurant)
            db.session.commit()
    for row in tqdm(download_zip_to_dict(kwargs["theatre_url"]), desc="Theatres"):
        if 'Адрес' not in row:
            theatre = models["theatres"](
                number=row[0],
                name=row[1],
                name_eng=row[2],
                type=row[3],
                address=row[4],
                phone=row[5],
                website=row[6],
                mail=row[7],
                notes=row[8],
                OGRN=row[9],
                INN=row[10],
                coords=row[11]
            )
            db.session.add(theatre)
            db.session.commit()
    for row in tqdm(download_zip_to_dict(kwargs["consulate_url"]), desc="Consulate"):
        if 'Адрес' not in row:
            consulate = models["consulate"](
                name="",
                number=row[0],
                state=row[1],
                type=row[2],
                address=row[3],
                leader=row[4],
                phone=row[5],
                coords=row[6]
            )
            db.session.add(consulate)
            db.session.commit()
    for row in tqdm(download_zip_to_dict(kwargs["zoo_url"]), desc="Zoo"):
        if 'Адрес' not in row:
            parsed = address_to_geo(row[3])
            zoo = models["zoo"](
                number=row[0],
                name=row[1],
                short_name=row[2],
                address=row[3],
                legal_address=row[4],
                district=row[5],
                subway=row[6],
                leader=row[7],
                phone=row[8],
                fax=row[9],
                working_hours=row[10],
                mail=row[11],
                municipal=row[12],
                INN=row[13],
                OGRN=row[14],
                coords=parsed
            )
            db.session.add(zoo)
            db.session.commit()
    db.session.close()


