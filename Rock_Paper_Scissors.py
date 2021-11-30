# Write your code here

import random

user_name = input("Enter your name: ")
print("Hello, " + user_name)

rating_file = open('rating.txt', "r+")

score = 0
for name in rating_file:
    if user_name in name:
        s = name.split()
        score = int(s[1])

print("Your rating: " + str(score))

rating_file.close()

rules = input().split(",")
if rules == [""]:
    rules = ["rock", "paper", "scissors"]

print("Okay, let's start")

while True:
    pc_choice = random.choice(rules)
    user_input = str(input())
    # check if user input exists in rules - create temp list by first adding
    # elements after chosen option and then adding elements before chosen option
    # if pc option is equal its a draw
    # if pc option in first half of this temp list then pc wins else user wins
    if user_input in rules:
        user_option_index = rules.index(user_input)
        left = user_option_index - 1
        right = user_option_index + 1
        temp_list = []
        first_half_index = 0
        while right < len(rules):
            temp_list.append(rules[right])
            right += 1
            first_half_index = len(temp_list)
        while left >= 0:
            temp_list.insert(first_half_index, rules[left])
            left -= 1

        first_half = temp_list[:round(len(temp_list) / 2)]
        second_half = temp_list[round(len(temp_list) / 2):]

        if pc_choice == user_input:
            print("There is a draw ({})".format(user_input))
            score += 50
        elif pc_choice in first_half:
            print("Sorry, but the computer chose {}".format(pc_choice))
        elif pc_choice in second_half:
            print("Well done. The computer chose {} and failed".format(pc_choice))
            score += 100

    if user_input == "!exit":
        print("Bye!")
        break
    elif user_input == "!rating":
        print(score)
    elif user_input not in rules:
        print("Invalid input")

rating_file.close()
