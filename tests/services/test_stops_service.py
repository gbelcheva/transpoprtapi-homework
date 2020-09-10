import pytest
import testing.postgresql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from services.bbox import Bbox, Coordinate
from services.data import stops_repo
from services.data.models import Stop
from services.stops_service import StopsService

MIN_LONG = 0.4
MIN_LAT = 53.
MAX_LONG = 0.7
MAX_LAT = 56.

BIG_BOX = Bbox(min_long=MIN_LONG, min_lat=MIN_LAT, max_long=MAX_LONG, max_lat=MAX_LAT)
EMPTY_BOX = Bbox(min_long=MIN_LONG+0.2, min_lat=MIN_LAT+0.7, max_long=MAX_LONG, max_lat=MAX_LAT)

stop1 = Stop(atcocode="atco1", commonname="common name1", longitude=MIN_LONG, latitude=MAX_LAT+0.5)
stop2 = Stop(atcocode="atco2", commonname="common name2", longitude=MAX_LONG, latitude=MIN_LAT+0.1)
stop3 = Stop(atcocode="atco3", commonname="common name3", longitude=MIN_LONG+0.1, latitude=MIN_LAT+0.2)
stop4 = Stop(atcocode="atco4", commonname="common name4", longitude=MIN_LONG+0.1, latitude=MIN_LAT+0.4)
stop5 = Stop(atcocode="atco5", commonname="common name5", longitude=MIN_LONG+0.1, latitude=MIN_LAT+0.6)


@pytest.fixture(scope='module')
def stops_service():
    with testing.postgresql.Postgresql() as postgresql:
        engine = create_engine(postgresql.url())
        Stop.metadata.create_all(engine)
        Session = sessionmaker(bind=engine, expire_on_commit=False)
        session = Session()
        session.add(stop1)
        session.add(stop2)
        session.add(stop3)
        session.add(stop4)
        session.add(stop5)
        session.flush()
        session.commit()

        from services.data.stops_repo import StopsRepo
        stops_repo.Session = Session
        yield StopsService(StopsRepo())
        session.close()


def test_stops_in_box_sorted(stops_service):
    number_closest_stops = 3
    actual_stops = stops_service.get_sorted_stops_in_bbox(BIG_BOX, number_closest_stops)

    expected_stops = [stop5, stop4, stop3]
    for i, actual_stop in enumerate(actual_stops):
        assert str(expected_stops[i]) == str(actual_stop)


def test_all_stops_outside_box(stops_service):
    number_closest_stops = 3
    actual_stops = stops_service.get_sorted_stops_in_bbox(EMPTY_BOX, number_closest_stops)

    assert len(actual_stops) == 0


def test_manhattan_distance_calculation():
    actual_distance = StopsService.calculate_manhattan_dist(Coordinate(long=0.236, lat=51.686),
                                                            Stop(atcocode="", commonname="", longitude=0.2,
                                                                 latitude=51.))

    expected_distance = 0.722
    assert expected_distance == actual_distance
