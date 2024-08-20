from dataclasses import dataclass
from typing import Tuple

# Airspace
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

# Altitude Bands:
@dataclass
class AltitudeBands:
    alt_band_low: AltitudeBand
    alt_band_mid: AltitudeBand
    alt_band_high: AltitudeBand

@dataclass
class AltitudeBand:
    min_alt: float
    max_alt: float

# Runway
@dataclass
class NewRunway:
    name: str
    dimentions: str
    surface: str
    coordinates: str
    elevation: float
    runway_heading: float
    displaced_threshold: int