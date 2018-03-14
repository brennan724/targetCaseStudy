# transit.py
#! /usr/bin/python3

# install requests
# install xmltodict https://github.com/martinblech/xmltodict

import requests
import sys

headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
base = 'http://svc.metrotransit.org/NexTrip/'

def scratch():
	# providers = requests.get(base + 'Providers', headers=headers)
	# print(providers.text)
	# print()
	# routes = requests.get(base + 'Routes', headers=headers)
	# print(routes.json())
	# print()
	directions = requests.get(base + 'Directions/901', headers=headers)
	print(directions.text)

def get_route_id(route_name):
	# gets the route ID based on the requested bus route.
	routes = requests.get(base + 'Routes', headers=headers).json()
	for route in routes:
		if route_name in route['Description']:
			return route['Route']

def get_stop_id(route_id, stop_name, direction):
	# gets the ID of the stop we are at.  needs the route because we need the list of stops
	# for the route to compare against to find our stop.
	directions = {'south':'1', 'east':'2', 'west':'3', 'north':'4'}
	direction = directions[direction]
	stops = requests.get(base + 'Stops/' + route_id + '/' + direction, headers=headers).json()
	for stop in stops:
		if stop_name in stop['Text']:
			return stop['Value']

def main():
    bus_route = sys.argv[1]
    bus_stop_name = sys.argv[2]
    direction = sys.argv[3]
    # scratch()
    route_id = get_route_id(bus_route)
    stop_id = get_stop_id(route_id, bus_stop_name, direction)
    print(stop_id)



main()