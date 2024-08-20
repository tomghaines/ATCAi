from dataclasses import dataclass
from typing import Tuple

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
    barometric_altitude: int
    GPS_altitude: int
    track: int
    ground_speed: int
    airspeed: int
    mach: int
    latitude: float
    longitude: float
    status: str