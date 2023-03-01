import string
import random

# obtain the number of people joining the party
try:
    print("Enter the number of friends joining (including you): ")
    how_many_people = int(input())
except:
    print("No one is joining for the party")
    exit()

if how_many_people <= 0: # Ensure more than 0 people
    print("No one is joining for the party")
    exit()

# Insert the friends names into a dictionary
friends_dict = dict()                       # Initializing dictionary.
print("")
print("Enter the name of every friend (including you), each on a new line: ")
for i in range(how_many_people):
    name = input()
    friends_dict[name] = 0


# Obtain total bill value
try:
    print("\nEnter the total bill. It will be split equally amongst the party members.")
    total_bill = int(input())
except:
    print("No one is joining for the party")
    exit()


# Lucky one Feature Implementation
try:
    print('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:')
    lucky_feature = input()
except:
    print("No one is going to be lucky")


if lucky_feature =="yes" or lucky_feature == "Yes":
    lucky_feature_on = 1    # Determine if the lucky_feature is on. Used to calculate bill splitting
    lucky_person_key = random.choice(list(friends_dict.keys()))
    print(f"{lucky_person_key} is the lucky one!")
else:
    lucky_feature_on = 0
    print("No one is going to be lucky")



# Split bill equally, and round to 2 digits.
split_bill = round(total_bill / (how_many_people - lucky_feature_on), 2)

for i in friends_dict: # Assigning bill values to users
    friends_dict[i] = split_bill

# Make sure the lucky one doesn't pay if the feature is on:
if lucky_feature_on == 1:
    friends_dict[lucky_person_key] = 0

# Print Statements
print("")
print(friends_dict)