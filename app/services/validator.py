def validate_long(long: float) -> bool:
    return True if -180.0 <= long <= 180.0 else False


def validate_lat(lat: float) -> bool:
    return True if -90.0 <= lat <= 90.0 else False


def require_parameter(param: str, param_name: str):
    if param is None:
        raise TypeError(f"Parameter {param_name} is required.")