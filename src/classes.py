from dataclasses import dataclass

# Airspace
@dataclass
class NewAirspace:
    name: str
    lat: float
    long: float
    alt: float
    runway: Runway
    coordinates: str
    elevation: str
    alt_bands: AltitudeBands

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
class Runway:
    name: str
    dimentions: str
    surface: str
    coordinates: str
    elevation: int
    runway_heading: float
    displaced_threshold: int
