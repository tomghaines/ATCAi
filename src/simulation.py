from test_airspace import heathrow_airspace, test_aircraft
import math

class Simulation:
    def __init__(self, airspace, aircraft):
        self.airspace = airspace
        self.aircraft = aircraft
    
    def simulate_departure(self):
        self.aircraft.status = "departing"
        while self.aircraft.current_alt < self.airspace.alt_bands.alt_band_mid.min_alt:
            self.aircraft.update_position(time_elapsed=1)  # 1 unit of time
            self.aircraft.update_altitude(rate_of_climb_or_descent=3000/60, time_elapsed=1)  # 3000 ft/min
            print(f"Aircraft {self.aircraft.aircraft_type} departing, current altitude: {self.aircraft.current_alt:.2f} feet")

        self.aircraft.status = "in-flight"
        print(f"Aircraft {self.aircraft.aircraft_type} has reached cruising altitude, status: {self.aircraft.status}")
    
    def simulate_arrival(self):
        self.aircraft.status = "arriving"
        while self.aircraft.current_alt > 0:
            self.aircraft.update_position(time_elapsed=1)  # 1 unit of time
            self.aircraft.update_altitude(rate_of_climb_or_descent=-3000/60, time_elapsed=1)  # 3000 ft/min descent
            print(f"Aircraft {self.aircraft.aircraft_type} arriving, current altitude: {self.aircraft.current_alt:.2f} feet")

        self.aircraft.status = "on-ground"
        print(f"Aircraft {self.aircraft.aircraft_type} has landed, status: {self.aircraft.status}")

# Run the simulation
simulation = Simulation(heathrow_airspace, test_aircraft)
simulation.simulate_departure()
simulation.simulate_arrival()
