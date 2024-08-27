print("enter a sentence")
sentence = input()
digit_count = 0
uppercase_count = 0
lowercase_count = 0
words = sentence.split()
word_count = len(words)
for char in sentence:
if char.isdigit():
digit_count += 1
elif char.isupper():
uppercase_count += 1
elif char.islower():
lowercase_count += 1

print(f"Number of words: {word_count}")
print(f"Number of digits: {digit_count}")
print(f"Number of uppercase letters:
{uppercase_count}")
print(f"Number of lowercase letters:
{lowercase_count}")
