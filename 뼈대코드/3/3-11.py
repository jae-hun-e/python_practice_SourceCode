from math import pi

def area_circle(radius, n):
    if radius > 0:
        area = pi * radius ** 2
        return round(area, n)
    else:
        return 0.0

print("Circle Area Calculator")
while True:
    r = input("Radius? ")
    p = input("Precision? ")
    area = area_circle(int(r),int(p))
    print("The area of a circle with radius", r, "is", area, ".")
print("Please come back again.")