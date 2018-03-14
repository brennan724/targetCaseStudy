# transit.py
#! /usr/bin/python3

# install requests
# install xmltodict https://github.com/martinblech/xmltodict

import requests
import sys
from datetime import datetime
import time

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
	# directions = {'south':'1', 'east':'2', 'west':'3', 'north':'4'}
	# direction = directions[direction]
	stops = requests.get(base + 'Stops/' + route_id + '/' + direction, headers=headers).json()
	for stop in stops:
		if stop_name in stop['Text']:
			return stop['Value']

def get_next_departure(route_id, direction_id, stop_id):
	departures = requests.get(base + route_id + '/' + direction_id + '/' + stop_id, headers=headers).json()
	return departures[0]
	# print(len(departures))
	# for departure in departures:
	# 	print(departure['DepartureTime'])

def time_remaining(next_departure):
	departure_time_unix = (int(next_departure['DepartureTime'][6:-7]) / 1000)
	# print(departure_time_unix)
	current_time = time.time()
	# print(current_time)
	remaining_seconds = departure_time_unix - current_time
	return remaining_seconds / 60

def main():
    bus_route = sys.argv[1]
    bus_stop_name = sys.argv[2]
    direction = sys.argv[3]
    directions = {'south':'1', 'east':'2', 'west':'3', 'north':'4'}
    direction_id = directions[direction]
    route_id = get_route_id(bus_route)
    stop_id = get_stop_id(route_id, bus_stop_name, direction_id)
    next_departure = get_next_departure(route_id, direction_id, stop_id)
    print(time_remaining(next_departure), 'minutes')



main()