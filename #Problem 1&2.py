#Problem 1
# Code to calculate the thickness when the paper is folded once

THICKNESS = 0.00008

folded_thickness = THICKNESS * 2**43

print("Thickness: {} meters".format(folded_thickness))

#Problem 2
# Convert meters to kilometers and display with two decimal places
print("Thickness: {: .2f} kilometers".format(folded_thickness / 1000))