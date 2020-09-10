import logging
from typing import List
from sqlalchemy import create_engine, and_, exc
from sqlalchemy.orm import sessionmaker

from services.bbox import Bbox
from services.data.models import Stop

log = logging.getLogger(__name__)

DB_STRING = "postgres+psycopg2://user:password@db:5432/user"  # ideally user and password contained in secrets
Session = sessionmaker(bind=create_engine(DB_STRING))


class StopsRepo(object):

    @staticmethod
    def read_stops_bbox(bbox: Bbox) -> List[Stop]:
        s = Session()
        stops = None
        try:
            stops = s.query(Stop) \
                .filter(and_(bbox.get_min_coord().get_long() <= Stop.longitude,
                             Stop.longitude <= bbox.get_max_coord().get_long(),
                             bbox.get_min_coord().get_lat() <= Stop.latitude,
                             Stop.latitude <= bbox.get_max_coord().get_lat())) \
                .all()
        except exc.SQLAlchemyError as e:
            log.error(f"Could not read stops. {str(e)}")
        return stops
