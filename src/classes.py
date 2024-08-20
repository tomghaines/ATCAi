class AltBand:
    def __init__(self, min_alt, max_alt):
        self.min_alt = min_alt
        self.max_alt = max_alt

class AltitudeBands:
    def __init__(self, alt_band_low, alt_band_mid, alt_band_high):
        self.alt_band_low = alt_band_low
        self.alt_band_mid = alt_band_mid
        self.alt_band_high = alt_band_high

class NewAirspace:
    def __init__(self, name, length, width, height, alt, alt_bands):
        self.name = name
        self.length = length
        self.width = width
        self.height = height
        self.alt = alt
        self.alt_bands = alt_bands