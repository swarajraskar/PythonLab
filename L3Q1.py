input_string = input("Enter your string: ")

char_dict = {}

for char in input_string:
    if char in char_dict:
        char_dict[char] += 1  
    else:
        char_dict[char] = 1   
print(char_dict)