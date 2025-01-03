""" other language array in python called list. 
But, difference is in list different type of data can be stored """

# list is mutable and string is immutable.
#because we can change the value of a list of a specific index but in string we can't

student=['sajib',102,21]
student[0]="rajib"  # In string we can't do this, we can just read the value
print(student)

# slicing property are same as string
print(student[1:2])

'''
If we do not assign starting value for slicing it will be automatically 
assign as zero for the ending value it will be last index.
'''
print(student[1:])

list1=[1,4,3,2,5]
list1.append(3)
list1.append(4)
# for adding multiple elemnt 
list1.extend([3,3,3])
print("Total 3: ", list1.count(3))
print("index of 5: ", list1.index(5))
list1.sort()  # if list1.sort(reverse=True) => descending ordered sort
print("sorted list: ", list1)

list2= list1.copy() #list2 is a new list with the same elements as list1, but it is stored in a different memory location.
print("copied list: ",list2)

# Here we need to know that sort , append, extend return None.

list2.reverse()
print("revresed list: ",list2)
list2.append(14)
list2.pop(4)  # the value of index 4 will be removed. If no index will be there, it will remove last element
list2.remove(14) # It will remove specific value. here, 3 will be removed from the list.
print("After remove list: ", list2)


