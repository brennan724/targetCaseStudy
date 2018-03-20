# targetCaseStudy

This repository contains code written in response to a Target Technical Assessment Case Study, involving API consumption.  The API used is the [Twin Cities Metro Area Transit API](http://svc.metrotransit.org/).

In order to run this code, please clone the repository and install [Python Requests](http://docs.python-requests.org/en/master/) by running `pip3 install requests`.  This requires pip, which ships with Python 2.7.9 (and later) and Python 3.4 (and later).

When given the appropriate parameters (described below), the output is the number of minutes until the next bus arrives, or a message if there is no scheduled bus, the route doesn't exist, or the stop doesn't exist.

In order to run the code itself, please run `python3 transit.py [Route Name] [Stop] [Direction]`.  The route name must be a substring of an actual route, and must be unique to that specific route.  The stop name must also be unique, and must exist on the previously stated route.  The direction must either be north, south, east, or west (all lowercase).  For example:
```
$ python3 transit.py "Maple Grove - U of M" "Willey Hall" "north"
172.01 minutes
```

There is a provided `tests.sh` file, which can only run (and be made executable) on a Unix machine.  To make it executable, run `chmod +x tests.sh` and then run the file by running `./tests.sh`.  This tests file merely runs the program multiple times on different sample input, printing out both the command that was run and the output of that command.  In order to ascertain correctness of the output, please look up the route, stop, and direction on [Metro Transit's website](https://www.metrotransit.org/).  In the upper right of the page, there is a box for NexTrip, which can be used to test the data.