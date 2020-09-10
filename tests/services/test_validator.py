from pytest import raises

from services import validator


def test_latitude_valid():
    latitude = -90.
    is_valid = validator.validate_lat(latitude)

    assert is_valid


def test_latitude_too_big_invalid():
    latitude = 91.
    is_valid = validator.validate_lat(latitude)

    assert not is_valid


def test_latitude_too_small_invalid():
    latitude = -91.
    is_valid = validator.validate_lat(latitude)

    assert not is_valid


def test_longitude_valid():
    longitude = 180.
    is_valid = validator.validate_long(longitude)

    assert is_valid


def test_longitude_too_big_invalid():
    longitude = 181.
    is_valid = validator.validate_long(longitude)

    assert not is_valid


def test_longitude_too_small_invalid():
    longitude = -181.
    is_valid = validator.validate_long(longitude)

    assert not is_valid


def test_require_parameter_missing_raises():
    with raises(TypeError):
        validator.require_parameter(None, "param_name")


def test_require_parameter_present_passes():
    validator.require_parameter("param", "param_name")
