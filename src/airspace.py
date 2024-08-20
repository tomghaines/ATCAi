from classes import AltitudeBand, AltitudeBands, NewAirspace

# Altitude Bands:
alt_b_low = AltitudeBand(min_alt=0, max_alt=50)
alt_b_mid = AltitudeBand(min_alt=50, max_alt=250)
alt_b_high = AltitudeBand(min_alt=250, max_alt=500)

alt_bands = AltitudeBands(alt_band_low=alt_b_low, alt_band_mid=alt_b_mid, alt_band_high=alt_b_high)

# Create new Airspace instance:
TestAirspace = NewAirspace(name="TEST", lat=20, long=34, alt=50, alt_bands=alt_bands)

print(TestAirspace)

