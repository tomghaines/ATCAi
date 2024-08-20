import datetime
import math
from classes import NewAircraft, NewAirspace
from airspace import TestAirspace
from aircraft import TestAircraft

DateTime = datetime.datetime.now()

class NewAircraft:
    def update_position(self, time_elapsed: float):
        distance_traveled = self.ground_speed * time_elapsed
        delta_lat = distance_traveled * math.cos(math.radians(self.heading))
        delta_long = distance_traveled * math.sin(math.radians(self.heading))

        self.current_lat += delta_lat
        self.current_long += delta_long

    def update_altitude(self, rate_of_climb_or_descent: float, time_elapsed: float):
        self.current_alt += rate_of_climb_or_descent * time_elapsed

class Simulation:
    def __init__(self, airspace, aircraft):
        self.airspace = airspace
        self.aircraft = aircraft
    
    def simulate_departure(self):
        self.aircraft.status = "departing"
        while self.aircraft.current_alt < self.airspace.alt_bands.alt_band_mid.min_alt:
            self.aircraft.update_position(time_elapsed=1) # 1 unit of time
            self.aircraft.update_altitude(rate_of_climb_or_descent=3000, time_elapsed=1) # 3000 ft/min
            print(f"Aircraft {self.aircraft.aircraft_type} departing, current altitude: {self.current_alt}")
        self.aircraft.status = "in-flight"