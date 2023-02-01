#!/usr/bin/env python3
# open-meteo weather API

import os
import requests
from datetime import datetime

geo_api = 'https://geocoding-api.open-meteo.com/v1/search'
weather_api = 'https://api.open-meteo.com/v1/forecast'


def query(url: str, payload: dict) -> dict:
    r = requests.get(url, params=payload)
    response = r.json()

    return response


def geo_query(payload: dict) -> dict:
    return query(geo_api, payload)['results']


def weather_query(payload: dict) -> dict:
    return query(weather_api, payload)


def get_latlong(postal_code: str) -> tuple:
    payload = {'name': postal_code}
    results = geo_query(payload)
    for r in results:
        if r['country_code'] == 'US':
            return r['latitude'], r['longitude']


def query_sunset(lat: float, long: float):
    payload = {
        'latitude': lat,
        'longitude': long,
        'timezone': 'America/New_York',
        'daily': 'sunset'
    }
    result =  weather_query(payload)

    return result['daily']['sunset']


def get_sunset():
    zip = 44273
    lat, long = get_latlong(zip)

    ss = query_sunset(lat, long)
    ts = ss[0]
    dt = datetime.strptime(ts, '%Y-%m-%dT%H:%M')

    return dt.minute, dt.hour


def main():
    print(get_sunset())


if __name__ == "__main__":
    main()
