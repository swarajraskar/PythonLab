s1 = input("Enter your string : ")
s2 = input("Enter your string : ")

l1 = list(s1)
l1[0],l1[1]=l1[1],l1[0]
l2 = list(s2)
l2[0],l2[1]=l2[1],l2[0]
s3 =''.join(l1)+" " +''.join(l2)

print(s3)
