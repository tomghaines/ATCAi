# Define altitude bands
alt_b_low = AltitudeBand(min_alt=0, max_alt=50)
alt_b_mid = AltitudeBand(min_alt=50, max_alt=250)
alt_b_high = AltitudeBand(min_alt=250, max_alt=500)
alt_bands = AltitudeBands(alt_band_low=alt_b_low, alt_band_mid=alt_b_mid, alt_band_high=alt_b_high)

# Define runways
runway_one = NewRunway(
    name="Runway 09L",
    dimensions="12799 x 164 feet / 3901 x 50 meters",
    surface="HARD",
    coordinates="N51°28.65' / W0°29.10'",
    elevation=79,
    runway_heading=0.89,
    displaced_threshold=1014
)