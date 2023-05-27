import math


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
