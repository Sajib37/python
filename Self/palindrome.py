list1 = list(input("Enter a string: "))
list2= list1.copy()
list2.reverse()
if(list1!=list2):
    print("It is not a palindrome")
else:
    print("It is a palindrome")
