"""
Name: problem2.py

Purpose: Tell whether you can take a summer vacation to Europe or California based on whether you get an 80% average and make $500 or not.

Author: Nguyen.D

Date: 2021-02-14
"""
average_percentage = int(input("What is your average grade percentage? "))
earned_money = int(input("How much did you make before the summer? "))

if average_percentage >= 80 and earned_money >= 500:
    print("You can go to Europe")
elif average_percentage >= 80 and earned_money < 500 :
    print("You can go to California.")
else:
  print("You can't go anywhere.")