a = (1,23,45,67,89)

print(type(a))

print(a.count(23)) # counts the number of occurrences of 23 in the tuple a

print(a.index(45)) # returns the index of the first occurrence of 45 in the tuple a

#print(a.index(100)) # raises a ValueError because 100 is not in the tuple a

print(len(a)) # returns the number of elements in the tuple a