# Author: Ziheng Wang
# Calculate factorial using a while loop
def factorial(n):
    if n == 0:
        return 1
    result = 1
    counter = 1
    while counter <= n:
        result *= counter
        counter += 1
    return result

number = int(input("Enter a number to calculate its factorial: "))
print(f"The factorial of {number} is {factorial(number)}")
