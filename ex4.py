# Author: Ziheng Wang
# Check discount eligibility based on age
age = int(input("Enter your age: "))

if age <= 19:
    print("You qualify for student discounts.")
elif 20 <= age <= 54:
    print("You qualify for no age discounts.")
else:
    print("You can receive senior discounts.")
