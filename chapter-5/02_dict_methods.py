marks = {
    "Harsh": 90,
    "Rohit": 85,
    "Sonia": 95,
    "Aman": 80
}

print(marks.items())  # dict_items([('Harsh', 90), ('Rohit', 85), ('Sonia', 95), ('Aman', 80)]  )

print(marks.keys())  # dict_keys(['Harsh', 'Rohit', 'Sonia', 'Aman'])

print(marks.values())  # dict_values([90, 85, 95, 80])

# marks.clear()  # This will clear the dictionary, making it empty

marks.update({"Harsh": 92, "Rohit": 88})  # This will update the values for Harsh and Rohit

print(marks.get("Sonia"))  # This will return the value for Sonia, which is 95

print (marks.get("Renuka"))  # This will return None since "Renuka" is not a key in the dictionary.
print(marks[Renuka])  # This will raise a KeyError since "Renuka" is not a key in the dictionary.

len(marks)  # This will return the number of key-value pairs in the dictionary, which is 4