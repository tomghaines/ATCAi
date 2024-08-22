from classes import NewAircraft

def GetMach(v):
    c = 343
    M = c / v
    return M

TestAircraft = NewAircraft(
    aircraft_type="Boeing 737 MAX 8-200 (B38M)",
    registration="EI-IHT",
    current_alt=37000,
    track=77,
    ground_speed=502,
    airspeed=502,
    mach=GetMach(502),
    current_lat=51.75723,
    current_long=-0.28253,
    heading="",
    status="on-ground"
)