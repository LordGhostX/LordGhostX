# calculator for area of circle
# formula for area = pi * r * r

import math

print("Enter the value of the circle radius to get the area")
while True:
    try:
        r = float(input("Enter the radius of the circle: "))
        break
    except:
        print("\nPlease enter a valid number")

area = math.pi * r * r
print("\nThe area of the circle with radius {} is {}".format(r, area))
