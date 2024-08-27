input_string= input("Enter your string: ")
my_list= (input_string.split())
print(my_list)
str2="/".join(my_list)
print(str2)
dict={
  "date":my_list[0],
  "month":my_list[1],
  "year":my_list[2]
}
print(dict)