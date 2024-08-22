from classes import AltitudeBand, AltitudeBands, NewAirspace, NewRunway

# Altitude Bands:
alt_b_low = AltitudeBand(min_alt=0, max_alt=50)
alt_b_mid = AltitudeBand(min_alt=50, max_alt=250)
alt_b_high = AltitudeBand(min_alt=250, max_alt=500)

alt_bands = AltitudeBands(alt_band_low=alt_b_low, alt_band_mid=alt_b_mid, alt_band_high=alt_b_high)

# Runway 09L/27R
RunwayOne = NewRunway(name="Runway 09L", dimensions="12799 x 164 feet / 3901 x 50 meters", surface="HARD", coordinates="N51°28.65' / W0°29.10'", elevation=79, runway_heading=0.89, displaced_threshold=1014)
RunwayTwo = NewRunway(name="Runway 27R", dimensions="12799 x 164 feet / 3901 x 50 meters", surface="HARD", coordinates="N51°28.66' / W0°26.00'", elevation=78, runway_heading=269, displaced_threshold=1014)

# Runway 09R/27L
RunwayThree = NewRunway(name="Runway 09R", dimensions="12799 x 164 feet / 3901 x 50 meters", surface="UNKNOWN", coordinates="N51°27.89' / W0°28.94'", elevation=75, runway_heading=0.89, displaced_threshold=1010)
RunwayFour = NewRunway(name="Runway 27L", dimensions="12799 x 164 feet / 3901 x 50 meters", surface="UNKNOWN", coordinates="N51°27.90' / W0°26.05'", elevation=77, runway_heading=269, displaced_threshold=1010)

# Create new Airspace instance:
TestAirspace = NewAirspace(
    name="HEATHROW",
    lat=20,
    long=34,
    alt=50,
    alt_bands=alt_bands,
    runway=(RunwayOne, RunwayTwo, RunwayThree, RunwayFour),
    coordinates="N51°28.65' / W0°27.68'",
    elevation=83.0
)
