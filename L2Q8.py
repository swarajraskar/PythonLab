import math
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))
hypotenuse = max(side1, side2, side3)
other_side1 = min(side1, side2, side3)

other_side2 = (side1 + side2 + side3) - hypotenuse -
other_side1
if hypotenuse ** 2 == other_side1 ** 2 + other_side2
** 2:
print("The triangle is a right triangle.")
else:
print("The triangle is not a right triangle.")
