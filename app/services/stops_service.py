import logging
from typing import List

from services.bbox import Bbox, Coordinate
from services.data.models import Stop
from services.data.stops_repo import StopsRepo

log = logging.getLogger(__name__)


class StopsService:
    def __init__(self, stops_repo: StopsRepo = None):
        log.info("Initializing stops service.")

        self.stops_repo = stops_repo or StopsRepo()

    def get_sorted_stops_in_bbox(self, bbox: Bbox, count: int = 20) -> List[Stop]:
        center = bbox.get_center()
        stops = self.stops_repo.read_stops_bbox(bbox)
        stops_manhattan_dist = {stop: self.calculate_manhattan_dist(center, stop) for stop in stops}
        stops_sorted_limited = [item[0] for item in
                                sorted(stops_manhattan_dist.items(), key=lambda item: item[1])[:count]]

        return stops_sorted_limited

    @staticmethod
    def calculate_manhattan_dist(center: Coordinate, stop: Stop) -> float:
        return abs(center.get_long() - stop.longitude) + abs(center.get_lat() - stop.latitude)
