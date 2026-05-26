# rad_to_deg.py
# RADIANS to DEGREES.
# Formula: degrees = radians x (180 / pi)

import math

def radians_to_degrees(radians):
    result = radians * (180 / math.pi)
    print(f"\n  {radians} radians = {result} degrees")
