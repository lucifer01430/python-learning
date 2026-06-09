#Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

words = {
    
    "Namaste": "Hello",
    "Shukriya": "Thank you",
    "Kripya": "Please",
    "Aap": "You",
    "Mujhe": "I",
    "Pyaar": "Love",
    "Dost": "Friend",
    "Khushi": "Happiness",
    "Sundar": "Beautiful",
    "Shakti": "Power"
}

word = input("Enter a Hindi word to look up its English translation: ")

print(words[word])