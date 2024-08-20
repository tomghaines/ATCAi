class AltBand:
    def __init__(self, min_alt, max_alt):
        self.min_alt = min_alt
        self.max_alt = max_alt

    def __repr__(self):
        return f"AltBand(MinAltitude={self.min_alt}, MaxAltitude={self.max_alt})"

class AltitudeBands:
    def __init__(self, alt_band_low, alt_band_mid, alt_band_high):
        self.alt_band_low = alt_band_low
        self.alt_band_mid = alt_band_mid
        self.alt_band_high = alt_band_high

    def __repr__(self):
        return (f"AltitudeBands(Low={self.alt_band_low}, "
                f"Mid={self.alt_band_mid}, "
                f"High={self.alt_band_high})")

class NewAirspace:
    def __init__(self, name, length, width, height, alt, alt_bands):
        self.name = name
        self.length = length
        self.width = width
        self.height = height
        self.alt = alt
        self.alt_bands = alt_bands

    def __repr__(self):
        return (f"Airspace(Name='{self.name}', Length={self.length}, "
                f"Width={self.width}, Height={self.height}, "
                f"Altitude={self.alt}, AltitudeBands={self.alt_bands})")

# Create instances of AltBand
my_airspace_altband_low = AltBand(min_alt=0, max_alt=10)
my_airspace_altband_mid = AltBand(min_alt=10, max_alt=50)
my_airspace_altband_high = AltBand(min_alt=50, max_alt=200)

# Create an instance of AltitudeBands
my_airspace_altitude_bands = AltitudeBands(alt_band_low=my_airspace_altband_low,
                                           alt_band_mid=my_airspace_altband_mid,
                                           alt_band_high=my_airspace_altband_high)

# Create an instance of NewAirspace
my_airspace = NewAirspace(name='LDN', length=25, width=10, height=20, alt=40,
                          alt_bands=my_airspace_altitude_bands)

# Print the instance of NewAirspace
print(my_airspace)
