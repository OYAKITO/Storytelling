"""
LETTER AND WORD COUNTER PROGRAM

This Python program prompts the user for a message and a specific letter, aiming to count occurrences of the designated letter in the given message while treating uppercase and lowercase versions as equivalent. The code not only counts letter occurrences but also extends its functionality to include a word count within the provided message, considering each distinct word regardless of case sensitivity. The final output delivers a clear message to the user, presenting both the occurrences of the specified letter (disregarding case) and the total word count in the entered message, thus providing a comprehensive summary of letter and word occurrences.
"""

print("Letter and Word Counter Program")

# Get name, input message and letter from the user
name = input("Enter your name: ").title().strip()
message = input("Enter a message: ")
letter = input("Enter a letter: ")

print("")

# Count occurrences of the specified letter (case-insensitive) - standardize
letter_count = message.lower().count(letter.lower())

# Count occurrences of words in the message
words = message.split()
word_count = len(words)

# Display the results
print(f"Hello, {name}!")
print(f"Your message has {str(letter_count)} {letter}'s in it.")
print(f"Your message has {word_count} words in it. The words are {words}")
