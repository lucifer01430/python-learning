a = (input("Enter a number: ")) #Here input works as string so that when we add two numbers it will concatenate them instead of adding them mathematically. To fix this we can use int() to convert the input to an integer.    
b = (input("Enter another number: "))

print("The concatination of two strings is: " , a+b)


a = int(input("Enter a number: ")) #Here we are converting the input to an integer so that we can add them mathematically.
b = int(input("Enter another number: "))    
print("The sum of the two numbers is: " , a+b)

