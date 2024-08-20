import datetime
import math

DateTime = datetime.datetime.now()

class NewAircraft:
    def update_position(self, time_elapsed: float):
        distance_traveled = self.ground_speed * time_elapsed
        delta_lat = distance_traveled * math.cos(math.radians(self.heading))
        delta_long = distance_traveled * math.sin(math.radians(self.heading))

        self.current_lat += delta_lat
        self.current_long += delta_long

    def update_altitude(self, rate_of_climb_or_descent: float, time_elapsed: float):
        self.current_alt += rate_of_climb_or_descent * time_elapsed
