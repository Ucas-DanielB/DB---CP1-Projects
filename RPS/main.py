#Write a program that lets a user play rock paper scissors against a computer. Using a while loop to let the game go until the user chooses to stop playing. 

#Note: you are going to want the loop to be while True, so that it can keep going forever until the user decides to quit. 

#Game needs to:

#1. Track score

#2. Let the user know if their input is invalid and have them try again (use a continue) 

#3. Use a break statement when the user chooses to exit

#4. Randomly select one of the 3 options for the computer and display it AFTER the user has selected their choice. 

import random

user_score = 0
computer_score = 0

print("If you would like to play rock paper scissors, please type 'rock', 'paper', or 'scissors'. Type 'leave' to exit.")


while True:
    user_choice = input("Your choice: ").lower()
    if user_choice == "leave":
        break
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid input. Try again.")
        continue

    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1


    print(f"Score - You: {user_score}, Computer: {computer_score}")


print("Thanks for playing!")
