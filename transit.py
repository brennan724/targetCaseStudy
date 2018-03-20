# transit.py
#! /usr/bin/python3

import requests
import sys
import time

headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
base = 'http://svc.metrotransit.org/NexTrip/'

def get_route_id(route_name):
    # gets the route ID based on the requested bus route by getting all routes
    # from API and then searching for the one that we are concerned about
    routes = requests.get(base + 'Routes', headers=headers).json()
    for route in routes:
        if route_name in route['Description']:
            return route['Route']
    print('There are no routes with this name')
    sys.exit()

def get_stop_id(route_id, stop_name, direction):
    # gets the ID of the stop we are at.  needs the route because we need the list of stops
    # for the route to compare against to find our stop.
    stops = requests.get(base + 'Stops/' + route_id + '/' + direction, headers=headers).json()
    for stop in stops:
        if stop_name in stop['Text']:
            return stop['Value']
    print('There are no stops with this name')
    sys.exit()

def get_next_departure(route_id, direction_id, stop_id):
    # gets information on the next departure based on route, direction, and stop
    # returns json object of next departure
    departures = requests.get(base + route_id + '/' + direction_id + '/' + stop_id, headers=headers).json()
    if len(departures) > 0:
        return departures[0]
    print('There are no scheduled departures from this stop')
    sys.exit()

def time_remaining(next_departure):
    # takes the json object containing info about the next departure and extracts the time
    # subtracts the current time from the departure time and returns the time remaining
    # json object departure time is in milliseconds
    departure_time_unix = (int(next_departure['DepartureTime'][6:-7]) / 1000)
    current_time = time.time()
    remaining_seconds = departure_time_unix - current_time
    return round(remaining_seconds / 60, 2)

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