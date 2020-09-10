# API service homework (Python3)

Application which “manages” a transport data source: reads the data from csv, stores the data in an SQL (Postgres) database and publishes the data as a JSON API.


## Description ##
The application is a composition of 2 containers:
- **db** based on [_postgres_](https://hub.docker.com/_/postgres) 
- **app** based on [_tiangolo/uwsgi-nginx-flask_](https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/)


## Requirements ##

[Docker](https://docs.docker.com/get-docker/)

## Data loading task ##

The database is bootstrapped in **Dockerfile-db** which downloads the data in a csv format. 
The csv file encoding is converted into UTF-8 (Unicode) which is supported by postgres.
The rest of the bootstrapping is done by postgres during initialization via two scripts located in _docker-entrypoint-initdb.d:

- _01_setup.sql_ - creates the table schema
- _02_load.sh_ - loads the csv data into the table

The scripts are executed in sorted name order.

## Endpoints exposed

This example app exposes the _/bus_stops_ endpoint, 
which retrieves 20 bus stops in a bounding box ordered by their Manhattan distance from the bounding box center:

    http://localhost/api/v1/bus_stops

with parameters

    min_long: string, representing float number
    min_lat: string, representing float number
    max_long: string, representing float number
    max_lat: string, representing float number

Example request:

    http://localhost/api/v1/bus_stops?min_long=-0.489&min_lat=51.28&max_long=0.236&max_lat=51.686
    
## Running the service

Run it with *docker-compose*:

    docker-compose up --build

The service should now be available on http://localhost
