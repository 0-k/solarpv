import math
import time

from generation import request_solar_data
from parameters import Technical


def calculate_min_distance(panel_width, panel_tilt, sun_height_at_noon):
    # Calculate the minimum distance between rows to avoid shadowing.
    # This is a simple approximation and assumes that the worst case shadowing occurs
    # when the sun is at its lowest point (winter solstice).
    # TODO: needs testing
    panel_tilt_radians = math.radians(panel_tilt)
    shadow_length = panel_width / math.tan(sun_height_at_noon)
    panel_height = panel_width * math.sin(panel_tilt_radians)
    total_distance = shadow_length + panel_height
    return total_distance


def energy_density_east_west(tilt):
    parameters_east = Technical(lat=50.01, lon=6.61, capacity=1.0, tilt=tilt, azim=90)
    parameters_west = Technical(lat=50.01, lon=6.61, capacity=1.0, tilt=tilt, azim=270)
    generation_east = request_solar_data(parameters_east).sum()
    generation_west = request_solar_data(parameters_west).sum()
    area = get_area(tilt)
    return (generation_east + generation_west) / 2 / area


def get_area(tilt):
    return math.cos(math.radians(tilt))


if __name__ == "__main__":
    for tilt in range(2, 50, 2):
        print(tilt, energy_density_east_west(tilt))
        time.sleep(1)
