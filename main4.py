#write a program to check the age enterd by the user is correct if there is an error in the value of the age enterd  by the user is even or odd
from datetime import datetime
current_year = datetime.now().year
age_input = input("Please enter your age: ")
year_input = input("Please enter your birth year: ")

age = int(age_input)
birth_year = int(year_input)

calculated_age = current_year - birth_year

if age == calculated_age:
    print("Age is correct.")
else:
    print("Age is incorrect.")
if age % 2 == 0:
    print("Your age is an even number.")
else:
    print("Your age is an odd number.")
