from classes import NewAircraft

def GetMach(v):
    c = 343
    M = c / v
    return M

TestAircraft = NewAircraft(
    aircraft_type="Boeing 737 MAX 8-200 (B38M)",
    registration="EI-IHT",
    barometric_altitude=37000,
    GPS_altitude=37000,
    track=77,
    ground_speed=502,
    airspeed=502,
    mach=GetMach(502),
    latitude=51.75723,
    longitude=-0.28253,
    heading="n/a",
    status="in-flight"
)

print(TestAircraft)