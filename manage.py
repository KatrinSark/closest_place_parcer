import os
from flask_script import Manager
from main.flask_app import app
from main.extensions import db
from main.tasks import update_database

manager = Manager(app)


@manager.command
def run():
    app.run(host="0.0.0.0", debug=True)


@manager.command
def initdb():
    db.create_all()
    db.session.commit()


@manager.command
def runtask():
    update_database(
        sport_url=os.getenv('SPORT_URL'),
        pass_table_url=os.getenv('PASS_TABLE_URL'),
        school_url=os.getenv('SCHOOL_URL'),
        kindergarden_url=os.getenv('KINDERGARDEN_URL'),
        vet_url=os.getenv('VET_URL'),
        clinic_url=os.getenv('CLINIC_URL'),
        exhibition_hall_url=os.getenv('EXHIBITION_HALL_URL'),
        hotel_url=os.getenv('HOTEL_URL'),
        sightseeing_url=os.getenv('SIGHTSEEING_URL'),
        cinema_url=os.getenv('CINEMA_URL'),
        museum_url=os.getenv('MUSEUM_URL'),
        restaurant_url=os.getenv('RESTAURANT_URL'),
        theatre_url=os.getenv('THEATRE_URL'),
        consulate_url=os.getenv('CONSULATE_URL'),
        zoo_url=os.getenv('ZOO_URL')
    )


if __name__=="__main__":
    manager.run()
