#! /usr/bin/env bash
set -e

#wget -O NaPTANcsv.zip "http://naptan.app.dft.gov.uk/DataRequest/Naptan.ashx?format=csv"
#mkdir -p /naptan && unzip -o NaPTANcsv.zip -d /naptan && rm NaPTANcsv.zip
#mv /naptan/Stops.csv Stops.csv && rm /naptan/* && mv Stops.csv /naptan/Stops.csv

psql -p 5432 -U user -c "COPY stops FROM '/naptan/Stops.csv' DELIMITER ',' CSV HEADER;"
