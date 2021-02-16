"""
Name: problem1.py

Purpose: Tell whether a triangle is a right angle triangle or not based on the side lengths

Author: Nguyen.D

Date: 2021-02-14
"""
side1 = float(input("Enter length of side 1: "))
side2 = float(input("Enter length of side 2: "))
side3 = float(input("Enter length of side 3: "))

side1_squared = side1**2
side2_squared = side2**2
side3_squared = side3**2

if (side1_squared)+(side2_squared)==(side3_squared):
  print("It is a right angle triangle.")
elif (side1_squared)+(side3_squared)==(side2_squared):
  print("It is a right angle triangle.")
elif (side2_squared)+(side3_squared)==(side1_squared):
  print("It is a right angle triangle.")
else:
  print("It is not a right angle triangle.")