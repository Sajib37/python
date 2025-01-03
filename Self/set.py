collection=set() #this is the way to initialize empty set, bcz,If we use {} => this will be dictionary

collection.add(2)
collection.add(3)
collection.add(4)
collection.add(3)


print(collection) # Duplicate value will be removed automatically

# the value of set can't be changed.But, we add new value in a set.
# previous value immutable, but, set is mutable.

set1={1,2,3}
set2={2,3,4}
print(set1.union(set2))
print(set1.intersection(set2))