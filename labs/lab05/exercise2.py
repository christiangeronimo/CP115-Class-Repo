import math
# Basic input and output
print("Welcome to the Circle Calculator!")
print("This program will calculate your area and circumferenceof the circle.")

# Getting user input (always returns a string)
radius = float(input("Enter your radius: "))

circle_area = math.pi * (radius ** 2)
circle_circumference =2 * math.pi * radius


# Formatted output using string concatenation
print()
print("Area: " + str(circle_area))
print("Circumference: " + str(circle_circumference))