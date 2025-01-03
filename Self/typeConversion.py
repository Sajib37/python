##implicit conversion
# Automatically or manually changing a value from one data type to another.
val1= 10
val2= 10.5
sum=val1+val2
print("type of sum: ", type(sum)) #sum will float automatically.


##explicit conversion (Type casting)
#Forcibly changing the data type of a value to a specified type.
val1= input('enter first value: ')
val2= 20
diff= val2-int(val1) #here need to typecasting, input function always take string.
print("Type of diff: ",type(diff))