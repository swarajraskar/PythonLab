test1 = float(input("Enter the mark for the first
test: "))
test2 = float(input("Enter the mark for the second
test: "))
test3 = float(input("Enter the mark for the third
test: "))
average1 = (test1 + test2) / 2
average2 = (test1 + test3) / 2
average3 = (test2 + test3) / 2
best_average = max(average1, average2, average3)
print(f"The best average of two out of three tests is:
{best_average}")
