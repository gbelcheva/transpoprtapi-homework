import logging

from flask import request, jsonify, Request

from main import app
from services.bbox import Bbox
from services.stops_service import StopsService
from services.validator import require_parameter

log = logging.getLogger(__name__)
stops_service = StopsService()


@app.route('/bus_stops')
def bus_stops():
    try:
        min_long = parse_param(request, "min_long")
        min_lat = parse_param(request, "min_lat")
        max_long = parse_param(request, "max_long")
        max_lat = parse_param(request, "max_lat")
        bbox = Bbox(min_long, min_lat, max_long, max_lat)
        stops = stops_service.get_sorted_stops_in_bbox(bbox)
        result = jsonify([stop.serialize for stop in stops])
    except (ValueError, TypeError) as e:
        log.error(str(e))
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        log.error(str(e))
        return jsonify({"error": "Unexpected error."}), 500

    return result


def parse_param(req: Request, param_name: str) -> float:
    param = req.args.get(param_name)
    require_parameter(param, param_name)
    return float(param)
