# tan.py
#  for TANGENT operation.
# tan(90) and tan(270) are undefined (division by zero in math).
# So we check for that before calculating.

import math

def tangent(angle_in_degrees):
    # (tan is undefined at 90, 270, 450... degrees)
    if angle_in_degrees % 180 == 90:
        print(f"\n  Error: tan({angle_in_degrees}) is undefined!")
    else:
        angle_in_radians = math.radians(angle_in_degrees)
        result = math.tan(angle_in_radians)
        result = round(result, 10)
        print(f"\n  tan({angle_in_degrees}) = {result}")
