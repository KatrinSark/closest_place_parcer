from dataclasses import dataclass

from sqlalchemy import Column, Integer, String
from main.extensions import db


@dataclass
class AbstractOrganization(db.Model):
    __abstract__ = True

    district: str = Column(String(250), nullable=True)
    name: str = Column(String(1000), nullable=False)
    short_name: str = Column(String(1000), nullable=True)
    address: str = Column(String(1000), nullable=False)
    coords: str = Column(String(250), nullable=False)
    leader: str = Column(String(250), nullable=True)
    phone: str = Column(String(250), nullable=True)
    fax: str = Column(String(250), nullable=True)
    mail: str = Column(String(250), nullable=True)
    municipal: str = Column(String(250), nullable=True)
    INN: str = Column(String(250), nullable=True)
    OGRN: str = Column(String(250), nullable=True)
    notes: str = Column(String(2000), nullable=True)
    website: str = Column(String(250), nullable=True)
    number: str = Column(String(250), nullable=True)
    working_hours: str = Column(String(1000), nullable=True)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


@dataclass
class School(AbstractOrganization):
    __tablename__ = 'school'
    id: int = Column(Integer, primary_key=True)


@dataclass
class KinderGarden(AbstractOrganization):
    __tablename__ = "kindergarden"
    id: int = Column(Integer, primary_key=True)
    nursery: str = Column(String(250), nullable=False)


@dataclass
class Vet(AbstractOrganization):
    __tablename__ = "vet"
    id: int = Column(Integer, primary_key=True)


@dataclass
class Clinic(AbstractOrganization):
    __tablename__ = "clinic"
    id: int = Column(Integer, primary_key=True)
    type: str = Column(String(250), nullable=False)


@dataclass
class PassTable(AbstractOrganization):
    __tablename__ = "passtable"
    id: int = Column(Integer, primary_key=True)
    division_number: str = Column(String(150), nullable=False)


@dataclass
class ExhibitionHall(AbstractOrganization):
    __tablename__ ='exhibition_hall'
    id: int = Column(Integer, primary_key=True)
    type: str = Column(String(250), nullable=True)
    name_eng: str = Column(String(250), nullable=True)
    description_eng: str = Column(String(1500), nullable=True)
    description: str = Column(String(1500), nullable=True)
    website: str = Column(String(250), nullable=True)


@dataclass
class Hotels(AbstractOrganization):
    __tablename__ ='hotels'
    id: int = Column(Integer, primary_key=True)
    type: str = Column(String(250), nullable=True)
    bedroom: str = Column(String(250), nullable=True)
    services: str = Column(String(5000), nullable=True)
    website: str = Column(String(250), nullable=True)
    room: str = Column(String(250), nullable=True)


@dataclass
class Sightseeing(AbstractOrganization):
    __tablename__ = 'sightseeing'
    id: int = Column(Integer, primary_key=True)
    type: str = Column(String(250), nullable=True)
    name_eng: str = Column(String(250), nullable=True)
    place_type: str = Column(String(250), nullable=True)
    description_eng: str = Column(String(5000), nullable=True)
    description: str = Column(String(5000), nullable=True)
    history: str = Column(String(5000), nullable=True)
    history_eng: str = Column(String(5000), nullable=True)
    working_hours_eng: str = Column(String(250), nullable=False)


@dataclass
class Cinema(AbstractOrganization):
    __tablename__ = 'cinema'
    id: int = Column(Integer, primary_key=True)
    type: str = Column(String(250), nullable=True)


@dataclass
class Museums(AbstractOrganization):
    __tablename__ = 'museums'
    id: int = Column(Integer, primary_key=True)
    name_eng: str = Column(String(250), nullable=True)
    county: str = Column(String(250), nullable=True)
    description_eng: str = Column(String(3000), nullable=True)
    description: str = Column(String(3000), nullable=True)
    type: str = Column(String(250), nullable=True)


@dataclass
class Restaurants(AbstractOrganization):
    __tablename__ = 'restaurants'
    id: int = Column(Integer, primary_key=True)
    name_eng: str = Column(String(250), nullable=True)
    kitchen: str = Column(String(2000), nullable=True)


@dataclass
class Theatres(AbstractOrganization):
    __tablename__ = 'theatres'
    id: int = Column(Integer, primary_key=True)
    name_eng: str = Column(String(250), nullable=True)
    type: str = Column(String(250), nullable=True)


@dataclass
class Consulate(AbstractOrganization):
    __tablename__ = 'consulate'
    id: int = Column(Integer, primary_key=True)
    type: str = Column(String(250), nullable=True)
    state: str = Column(String(250), nullable=True)


@dataclass
class Zoo(AbstractOrganization):
    __tablename__ = 'zoo'
    id: int = Column(Integer, primary_key=True)
    subway: str = Column(String(250), nullable=True)


@dataclass
class Sport(AbstractOrganization):
    __tablename__ = 'sport'
    id: float = Column(Integer, primary_key=True)
    type: str = Column(String(500), nullable=True)
    address_info: str = Column(String(1000), nullable=False)
    subway: str = Column(String(500), nullable=True)
    status: str = Column(String(500), nullable=True)
    inventory: str = Column(String(7), nullable=True)
    instructor: str = Column(String(7), nullable=True)
    dressing_room: str = Column(String(7), nullable=True)
    baggage_room: str = Column(String(7), nullable=True)
    other: str = Column(String(500), nullable=True)


@dataclass
class FishSpots(db.Model):
    __tablename__ = "fish_spots"
    id: int = Column(Integer, primary_key=True)
    address: str = Column(String(1000))
    coords: str = Column(String(50))
    district: str = Column(String(250))
    url: str = Column(String(250))
    subway: str = Column(String(250))


models = {
    'fish_spot': FishSpots,
    'clinic': Clinic,
    'school':School,
    'kindergarden': KinderGarden,
    'vet': Vet,
    'passtable': PassTable,
    'exhibition_hall': ExhibitionHall,
    'hotels': Hotels,
    'sightseeing': Sightseeing,
    'cinema': Cinema,
    'museums': Museums,
    'restaurants': Restaurants,
    'theatres': Theatres,
    'consulate': Consulate,
    'zoo': Zoo,
    'sport': Sport
}
