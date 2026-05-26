# deg_to_rad.py
# converts DEGREES to RADIANS.


import math

def degrees_to_radians(degrees):
    result = degrees * (math.pi / 180)
    print(f"\n  {degrees} degrees = {result} radians")
