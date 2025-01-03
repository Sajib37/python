# https://www.w3schools.com/python/python_ref_string.asp
# explore the link to learn more methods

#concatination
str1= "sajib"
str2= "hasan"
finalstr= str1+str2

# 1. len()
print(len(str2))

# indexing
print(str2[2])

#slicing
print(str2[2:4])

# negative Slicing
print("negative slicing: ",str2[-5:-1])
print("negative slicing2: ",str2[-5:0])


str3= "bangladesh is agricultural country and country"
print(str3.endswith("ry"))
print(str3.capitalize())  #capitalizae first character
print(str3.replace("country",'desh'))
print(str3.find("is"))  #returns 1st index of 1st occurrence => If Not Found: Returns -1
print(str3.index("is")) # If Not Found: Raises a ValueError.
print(str3.count('country'))    #counts the occurrence of substr in string
print(str3.title())     #capitalize every first charcter of every word.
print(str3.casefold())  #Converts string into lower case  Converts all uppercase characters to lowercase, and performs more aggressive case conversion for special or locale-specific characters.
print(str3.lower())     #Limitation: Does not handle special cases like non-English characters


# conditional statement
marks= int(input("Enter marks: "))

if(marks>=80):
    print("Grade: A+")
elif(marks>=70):
    print("Grade: A+")
elif(marks>=60):
    print("Grade: A-")
elif(marks>=50):
    print("Grade: B")
elif(marks>=40):
    print("Grade: C")
elif(marks>=33):
    print("Grade: D")
else:
    print("Grade: F")