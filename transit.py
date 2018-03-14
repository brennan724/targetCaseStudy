# transit.py
#! /usr/bin/python3

# install requests
# install xmltodict https://github.com/martinblech/xmltodict

import requests
import sys

headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
base = 'http://svc.metrotransit.org/NexTrip/'
providers = requests.get(base + 'Providers', headers=headers)
print(providers.text)
print()
routes = requests.get(base + 'Routes', headers=headers)
print(routes.text)
print()
directions = requests.get(base + 'Directions/1', headers=headers)
print(directions.text)

def main():
    bus_route = sys.argv[1]
    bus_stop_name = sys.argv[2]
    direction = sys.argv[3]


main()