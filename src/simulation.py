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

    def update_altitude(self, rate_of_climb_or_decent: float, time_elapsed: float):
        self.current_alt += rate_of_climb_or_decent * time_elapsed

class Simulation:
    def __init__(self, airspace, aircraft):
        self.airspace = airspace
        self.aircraft = aircraft
    
    def simulate_departure(self):
        self.aircraft.status = "departing"
        while self.aircraft.current_alt < self.airspace.alt_bands.alt_band_mid.min_alt:
            self.aircraft.update_position(time_elapsed=1) # 1 unit of time
            self.aircraft.update_altitude(rate_of_climb_or_decent=3000/60, time_elapsed=1) # 3000 ft/min, converted to ft/second

            # Output the current state
            print(f"Aircraft {self/aircraft.aircraft_type} departing, current altitude: {self.current_alt:.2f} feet, position: ({self.aircraft.current_lat:.4f}, {self.aircraft.current_long:.4f})")

        self.aircraft.status = "in-flight"
        print(f"Aircraft {self.aircraft.aircraft_type} has reached cruising altitude, status: {self.aircraft.status}")

simulation = Simulation(TestAirspace, TestAircraft)
simulation.simulate_departure()