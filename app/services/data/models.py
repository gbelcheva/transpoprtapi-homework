from sqlalchemy import Column, Text, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Stop(Base):

    __tablename__ = 'stops'

    atcocode = Column(Text, primary_key=True)
    commonname = Column(Text)
    longitude = Column(Float)
    latitude = Column(Float)

    def __str__(self):
        return "Stop(ATCO code='{}', common name='{}', lat={}, long={})"\
            .format(self.atcocode, self.commonname, self.latitude, self.longitude)

    @property
    def serialize(self):
        return {
            'atco_code': self.atcocode,
            'common_name': self.commonname,
            'longitude': self.longitude,
            'latitude': self.latitude
        }
