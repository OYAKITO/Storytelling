"""
YES OR NO POLLING PROGRAM
This Python program will conduct a poll on a yes or no issue. Upon starting the program, a user will be prompted for an issue to vote on, the number of voters, and a password to view the poll results. The program will then conduct the poll. Each time a user votes, the program will ask for the voters full name to verify that they have not yet voted. If the voter has not yet voted, they will be presented with the issue and can vote yes or no. The vote will be recorded. Once the number of voters specified by the user has been reached, the poll will close and a summary will be displayed. If the user enters the correct password a result of each voters name and how they voted will be displayed.
"""

print("Welcome to the Issue Polling Program!")

# Get user input
issue = input("What is the yes or no issue you will be voting on today: ")
vote_number = int(input("What is the number of voters you will allow on the issue: "))
password = input("Enter a password for the polling results: ")

# Initialize variables
yes_votes = 0
no_votes = 0
results = {}

# Simulate voting
for _ in range(vote_number):
    name = input("\nEnter your full name: ").title().strip()

    if name in results:
        print("Sorry, it seems that someone with that name has already voted.")
    else:
        print("Here is our issue: " + issue)
        choice = input("What do you think... yes or no? ").lower().strip()

        if choice in {'yes', 'y'}:
            choice = 'yes'
            yes_votes += 1
        elif choice in {'no', 'n'}:
            choice = 'no'
            no_votes += 1
        else:
            print("That is not a yes or no answer, but okay...")

        # Add vote to the results dictionary
        results[name] = choice
        print(f"Thank you {name}! Your vote of {results[name]} has been recorded.")

# Show who actually voted
total_votes = len(results)
print(f"\nThe following {total_votes} people voted:")
for key in results:
    print(key)

# Summarize the voting results
print(f"\nOn the following issue: {issue}")
if yes_votes > no_votes:
    print(f"Yes wins! {yes_votes} votes to {no_votes}.")
elif no_votes > yes_votes:
    print(f"No wins! {no_votes} votes to {yes_votes}.")
else:
    print(f"It was a tie! {no_votes} votes to {yes_votes}.")

# Allow the admin to see the actual votes
guess = input("\nTo see the voting results enter the admin password: ")
if guess == password:
    for key, value in results.items():
        print(f"Voter: {key}\t\t\tVote: {value}")
else:
    print("Sorry, that is not the correct password. Goodbye...")

print("\nThank you for using the Polling App.")
