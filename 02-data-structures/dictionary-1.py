"""
THESAURUS PROGRAM

This Python program simulates a thesaurus. The program will present a user with a list of words that the thesaurus contains. Based on the users choice, you will randomly present them with a synonym for their chosen word. Lastly, the program will display all of the potential synonyms for each word in the thesaurus.
"""

import random

# Define the thesaurus
thesaurus = {
    "hot": ['balmy', 'summery', 'tropical', 'boiling', 'scorching'],
    "cold": ['chilly', 'cool', 'freezing', 'frigid', 'polar'],
    "happy": ['content', 'cheery', 'merry', 'jovial', 'jocular'],
    "sad": ['unhappy', 'downcast', 'miserable', 'glum', 'melancholy'],
}

# Print welcome information
print("Welcome to the Thesaurus App!")
print("\nChoose a word from the thesaurus and I will give you a synonym.")
print("\nHere are the words in the thesaurus: ")
for key in thesaurus.keys():
    print("\t-" + key)

# Get user input
choice = input("\nWhat word would you like a synonym for: ").lower().strip()

# Provide a random synonym
if choice in thesaurus:
    synonym = random.choice(thesaurus[choice])
    print(f"A synonym for {choice} is {synonym}.")
else:
    print("I'm sorry, that word is not currently in the thesaurus.")

# Get user input to see the whole thesaurus
choice = input("\nWould you like to see the whole thesaurus (yes/no): ").lower().strip()

# Show all values in the thesaurus
if choice == 'yes':
    for key, values in thesaurus.items():
        print(f"\n{key.title()} synonyms are:")
        for value in values:
            print("\t-" + value)
else:
    print("\nThank you for using the thesaurus!")
