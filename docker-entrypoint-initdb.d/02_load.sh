#! /usr/bin/env bash
set -e

psql -p 5432 -U user -c "COPY stops FROM '/naptan/Stops.csv' DELIMITER ',' CSV HEADER;"
