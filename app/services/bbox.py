from __future__ import annotations

from services import validator


class Bbox:
    def __init__(self, min_long: float, min_lat: float, max_long: float, max_lat: float):
        self.min_coord = Coordinate(min_long, min_lat)
        self.max_coord = Coordinate(max_long, max_lat)
        self.validate_box(min_long, min_lat, max_long, max_lat)
        self.center = None

    def get_min_coord(self) -> Coordinate:
        return self.min_coord

    def get_max_coord(self) -> Coordinate:
        return self.max_coord

    def get_center(self) -> Coordinate:
        if self.center is None:
            self.center = Coordinate((self.min_coord.long + self.max_coord.long) / 2,
                                     (self.min_coord.lat + self.max_coord.lat) / 2)

        return self.center

    @staticmethod
    def validate_box(min_long, min_lat, max_long, max_lat):
        if not (min_long < max_long and min_lat < max_lat):
            raise ValueError(
                f"Box coordinates are invalid - "
                f"min_long {min_long}, min_lat {min_lat}, max_long {max_long}, max_lat {max_lat}.")


class Coordinate:
    def __init__(self, long: float, lat: float):
        self.validate_coord(long, lat)
        self.long = long
        self.lat = lat

    def get_long(self) -> float:
        return self.long

    def get_lat(self) -> float:
        return self.lat

    @staticmethod
    def validate_coord(long, lat):
        if not (validator.validate_long(long) and validator.validate_long(lat)):
            raise ValueError(
                f"Coordinate is invalid - longitude {long}, latitude {lat}.")
