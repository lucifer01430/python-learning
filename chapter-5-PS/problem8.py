#Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique. If languages of two friends are same; what will happen to the program in problem 6? 


#just here put the same language for 2 friends and see the output.

dict = {}

name = input("Enter your name: ")
language = input("Enter your favorite language: ")
dict.update({name: language}) 

name = input("Enter your name: ")
language = input("Enter your favorite language: ")
dict.update({name: language}) 

name = input("Enter your name: ")
language = input("Enter your favorite language: ")
dict.update({name: language}) 

name = input("Enter your name: ")
language = input("Enter your favorite language: ")
dict.update({name: language}) 

print(dict)