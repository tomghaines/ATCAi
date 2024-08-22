from dataclasses import dataclass
from typing import Tuple
import math

# Airspace
@dataclass
class AltitudeBand:
    min_alt: float
    max_alt: float

@dataclass
class AltitudeBands:
    alt_band_low: AltitudeBand
    alt_band_mid: AltitudeBand
    alt_band_high: AltitudeBand

@dataclass
class NewRunway:
    name: str
    dimensions: str
    surface: str
    coordinates: str
    elevation: float
    runway_heading: float
    displaced_threshold: float

@dataclass
class NewAirspace:
    name: str
    lat: float
    long: float
    alt: float
    alt_bands: AltitudeBands
    runway: Tuple[NewRunway, NewRunway, NewRunway, NewRunway]
    coordinates: str
    elevation: float

# Aircraft
@dataclass
class NewAircraft:
    aircraft_type: str
    registration: str
    track: int
    airspeed: float
    ground_speed: float
    mach: float
    current_lat: float
    current_long: float
    current_alt: float
    heading: float
    status: str
    
    def update_position(self, time_elapsed: float):
        distance_traveled = self.ground_speed * time_elapsed
        delta_lat = distance_traveled * math.cos(math.radians(self.heading))
        delta_long = distance_traveled * math.sin(math.radians(self.heading))

        self.current_lat += delta_lat
        self.current_long += delta_long

    def update_altitude(self, rate_of_climb_or_descent: float, time_elapsed: float):
        self.current_alt += rate_of_climb_or_descent * time_elapsed
