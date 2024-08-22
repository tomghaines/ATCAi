import datetime
import math
from classes import NewAircraft, NewAirspace
from airspace import TestAirspace
from aircraft import TestAircraft

DateTime = datetime.datetime.now()

class NewAircraft:
    def __init__(self, aircraft_type, current_lat, current_long, current_alt, ground_speed, heading):
        self.aircraft_type = aircraft_type
        self.current_lat = current_lat
        self.current_long = current_long
        self.current_alt = current_alt
        self.ground_speed = ground_speed
        self.heading = heading
        self.status = "on-ground"
    
    def update_position(self, time_elapsed: float):
        distance_traveled = self.ground_speed * time_elapsed
        delta_lat = distanced_traveled * math.cos(math.radians(self.heading))
        delta_long = distance_traveled * math.sin(math.radians(self.heading))

        self.current_lat += delta_lat
        self.current_long += delta_long
