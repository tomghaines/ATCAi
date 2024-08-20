from dataclasses import dataclass

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
class NewAirspace:
    name: str
    lat: float
    long: float
    alt: float
    alt_bands: AltitudeBands

    