#Write a program to accept marks of 6 students and display them in a sorted manner. 

Marks = []

Student1 = int(input("Enter the marks of student 1: "))
Marks.append(Student1)

Student2 = int(input("Enter the marks of student 2: "))
Marks.append(Student2)

Student3 = int(input("Enter the marks of student 3: "))
Marks.append(Student3)

Student4 = int(input("Enter the marks of student 4: "))
Marks.append(Student4)

Student5 = int(input("Enter the marks of student 5: "))
Marks.append(Student5)

Student6 = int(input("Enter the marks of student 6: "))
Marks.append(Student6)

Marks.sort()
print ("The marks of the students are: ", Marks)