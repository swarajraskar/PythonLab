number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))
if number1 >= number2 and number1 >= number3:
largest_number = number1
elif number2 >= number1 and number2 >= number3:
largest_number = number2
else:
largest_number = number3
print(f"The largest number among {number1}, {number2},
and {number3} is: {largest_number}")
