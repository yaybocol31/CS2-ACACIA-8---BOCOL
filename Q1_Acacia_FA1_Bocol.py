import math

x1 = int(input ("what is the value of x1?")) # x1 is the first number from the coordinates of point A.

x2 = int(input ("what is the value of x2?")) # x2 is the first number from the coordinates of point B.

y1 = int(input ("what is the value of y1?")) # y1 is the second number from the coordinates of point A.

y2 = int(input ("what is the value of y2?")) # y2 is the second number from the coordinates of point B.

d = math.sqrt((math.pow((x2-x1),2))+(math.pow((y2-y1),2)))
print(d)

"""Because libraries are like shortcuts that make coding easier and more efficient without hvaing to type every code manually.
The math library helped simplify things for my program with its pre-written code, making it easier for the computer to understand without having to type everything by hand.
The library helped solved the math equation easier and made things like square root and power efficient and more understandable.
It would have been more diffucult because it would mean we would have to type everything by hand."""
