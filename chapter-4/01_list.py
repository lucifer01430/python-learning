friends = ["Harsh","Aman",9,"Apple",True,"Banana","Akash"]

print(friends[0]) # Harsh
print(friends[1]) # Aman

friends[0] = "Rohit" # Change Harsh to Rohit
print(friends) 

print(friends[1:5]) # List Slicing - from index 1 to 4 (5 is exclusive)
print(friends[:4]) # List Slicing - from start to index 3 (4 is exclusive)