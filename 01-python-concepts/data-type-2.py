"""
MPH AND MPS CONVERSION PROGRAM

This Python program will convert any given speed in miles per hour to a more metric friendly unit of meters per second. All calculations should be rounded to a set decimal precision of 4 decimal places.
"""

print("MPH and MPS Conversion Program")
# Gather user input
mph = float(input("\nWhat is your speed in miles per hour? "))

# Convert to mps
mps = mph*0.4474
mps = round(mps, 4)

print(f"You converted {str(mph)} miles per hour to {str(mps)} miles per second.")