# Test Expenses Travel

# Author@Richard Whittle

# 21/12/2019 

# first draft

'''
This is the test file for the travel espenses algorythm. This tests the 
following functions
'''

#from current_income_expenses import *
from calculate_expenses import * # car_travel_per_trip
# from expense_calc_inputs import *

# Test Car 
test_nil = 0
test_short = 10
test_medium = 25
test_long = 75


assert car_travel_per_trip(test_nil) == 0
assert car_travel_per_trip(test_short) == 4.5
assert car_travel_per_trip(test_medium) == 11.25
assert car_travel_per_trip(test_long) == 33.75

#Test Train
train_fare_nil = 0
train_fare_low = 4.75
train_fare_medium = 10
train_fare_high = 105.25
train_no_trips = 0
train_trips_weekly = 1
train_trips_daily = 5

# Train assertions

assert train_ticket_return(train_fare_nil, train_no_trips) == 0
assert train_ticket_return(train_fare_low, train_no_trips) == 0
assert train_ticket_return(train_fare_medium, train_no_trips) == 0
assert train_ticket_return(train_fare_high, train_no_trips) == 0

#train Assert daily tests

assert train_ticket_return(train_fare_nil, train_trips_daily) == 0
assert train_ticket_return(train_fare_low, train_trips_daily) == 23.75
assert train_ticket_return(train_fare_medium, train_trips_daily) == 50
assert train_ticket_return(train_fare_high, train_trips_daily) == 526.25

#Train Assert weekly tests

assert train_ticket_return(train_fare_nil, train_trips_weekly) == 0
assert train_ticket_return(train_fare_low, train_trips_weekly ) == 4.75
assert train_ticket_return(train_fare_medium, train_trips_weekly) == 10
assert train_ticket_return(train_fare_high, train_trips_weekly) == 105.25

# Test Bus
bus_fare_nil = 0
bus_fare_low = 1.20
bus_fare_medium = 3.50
bus_fare_high = 25.50

bus_no_trips = 0
bus_trips_daily = 5
bus_trips_weekly = 1

# Bus Assertions
assert bus_fare_nil * bus_no_trips == 0
assert bus_fare_low * bus_no_trips == 0
assert bus_fare_medium * bus_no_trips == 0
assert bus_fare_high * bus_no_trips == 0

assert bus_fare_nil * bus_trips_daily == 0
assert bus_fare_low * bus_trips_daily  == 6
assert bus_fare_medium * bus_trips_daily == 17.5
assert bus_fare_high * bus_trips_daily == 127.5

assert bus_fare_nil * bus_trips_weekly == 0
assert bus_fare_low * bus_trips_weekly == 1.2
assert bus_fare_medium * bus_trips_weekly == 3.5
assert bus_fare_high * bus_trips_weekly == 25.5

# Test Ferry
'''
undecided if I will do this or class this under other tests, the logic should be fine though
'''

# Test other
