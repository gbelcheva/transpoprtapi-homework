import json
from unittest import mock

import pytest

import main
from services.data.models import Stop


@pytest.fixture()
def flask_app():
    return main.app.test_client()


@mock.patch("api.views.stops_service.get_sorted_stops_in_bbox", return_value=[])
def test_valid_box_empty_stops_response(stops_service_mock, flask_app):
    response = flask_app.get("/api/v1/bus_stops?min_long=-0.489&min_lat=51.28&max_long=0.236&max_lat=55.686")
    assert response.status_code == 200
    json_response = json.loads(response.data.decode("utf-8"))

    assert json_response == []


@mock.patch("api.views.stops_service.get_sorted_stops_in_bbox",
            return_value=[Stop(atcocode="atco1", commonname="common name1", longitude=55.5, latitude=0.5),
                          Stop(atcocode="atco2", commonname="common name2", longitude=55.6, latitude=0.6)])
def test_valid_box_stops_response(stops_service_mock, flask_app):
    response = flask_app.get("/api/v1/bus_stops?min_long=-0.489&min_lat=51.28&max_long=0.236&max_lat=55.686")
    assert response.status_code == 200
    json_response = json.loads(response.data.decode("utf-8"))

    assert json_response == [{
            'atco_code': "atco1",
            'common_name': "common name1",
            'longitude': 55.5,
            'latitude': 0.5
        },
        {
            'atco_code': "atco2",
            'common_name': "common name2",
            'longitude': 55.6,
            'latitude': 0.6
        }
    ]


@mock.patch("api.views.stops_service")
def test_invalid_box_400(stops_service_mock, flask_app):
    response = flask_app.get("/api/v1/bus_stops?min_long=-0.489&min_lat=56.28&max_long=0.236&max_lat=55.686")
    assert response.status_code == 400
    json_response = json.loads(response.data.decode("utf-8"))

    assert json_response == {
        "error": "Box coordinates are invalid - min_long -0.489, min_lat 56.28, max_long 0.236, max_lat 55.686."}


@mock.patch("api.views.stops_service")
def test_invalid_coordinate_400(stops_service_mock, flask_app):
    response = flask_app.get("/api/v1/bus_stops?min_long=-0.489&min_lat=56.28&max_long=0.236&max_lat=181.686")
    assert response.status_code == 400
    json_response = json.loads(response.data.decode("utf-8"))

    assert json_response == {"error": "Coordinate is invalid - longitude 0.236, latitude 181.686."}


@mock.patch("api.views.stops_service")
def test_invalid_coordinate_format_400(stops_service_mock, flask_app):
    response = flask_app.get("/api/v1/bus_stops?min_long=-0.489&min_lat=56.28&max_long=0.236&max_lat=57f")
    assert response.status_code == 400
    json_response = json.loads(response.data.decode("utf-8"))

    assert json_response == {"error": "could not convert string to float: '57f'"}


@mock.patch("api.views.stops_service")
def test_missing_parameter_400(stops_service_mock, flask_app):
    response = flask_app.get("/api/v1/bus_stops?min_long=-0.489&min_lat=56.28&max_long=0.236")
    assert response.status_code == 400
    json_response = json.loads(response.data.decode("utf-8"))

    assert json_response == {"error": "Parameter max_lat is required."}


@mock.patch("api.views.stops_service.get_sorted_stops_in_bbox", side_effect=Exception("yikes"))
def test_unknown_error_500(stops_service_mock, flask_app):
    response = flask_app.get("/api/v1/bus_stops?min_long=-0.489&min_lat=51.28&max_long=0.236&max_lat=55.686")
    assert response.status_code == 500
    json_response = json.loads(response.data.decode("utf-8"))

    assert json_response == {"error": "Unexpected error."}
