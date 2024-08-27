number = input("Enter a number: ")
if number == number[::-1]:
print(f"{number} is a palindrome.")
else:
print(f"{number} is not a palindrome.")
digit_count = {}
for digit in number:
if digit in digit_count:
digit_count[digit] += 1
else:
digit_count[digit] = 1
print("Occurrences of each digit:")
for digit, count in digit_count.items():
print(f"Digit {digit}: {count} time(s)")
