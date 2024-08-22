from classes import AltitudeBand, AltitudeBands, NewAirspace, NewRunway, NewAircraft

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

runway_two = NewRunway(
    name="Runway 27R",
    dimensions="12799 x 164 feet / 3901 x 50 meters",
    surface="HARD",
    coordinates="N51°28.66' / W0°26.00'",
    elevation=78,
    runway_heading=269,
    displaced_threshold=1014
)

runway_three = NewRunway(
    name="Runway 09R",
    dimensions="12799 x 164 feet / 3901 x 50 meters",
    surface="UNKNOWN",
    coordinates="N51°27.89' / W0°28.94'",
    elevation=75,
    runway_heading=0.89,
    displaced_threshold=1010
)

runway_four = NewRunway(
    name="Runway 27L",
    dimensions="12799 x 164 feet / 3901 x 50 meters",
    surface="UNKNOWN",
    coordinates="N51°27.90' / W0°26.05'",
    elevation=77,
    runway_heading=269,
    displaced_threshold=1010
)


# Define an aircraft
def get_mach(v):
    c = 343  # Speed of sound in m/s at sea level
    return v / c

test_aircraft = NewAircraft(
    aircraft_type="Boeing 737 MAX 8-200 (B38M)",
    registration="EI-IHT",
    track=77,
    airspeed=502,  # Example airspeed in knots
    ground_speed=502,
    mach=get_mach(502),
    current_lat=51.4706,
    current_long=-0.461941,
    current_alt=0,
    heading=90,  # Example heading in degrees
    status="on-ground"
)