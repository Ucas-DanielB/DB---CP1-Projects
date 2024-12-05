#Create a multiple choice quiz game that tests the user's knowledge on a topic (please pick a school appropriate topic and yes all of the questions need to be on that topic!) 

#Give the user 5 multiple choice questions with A, B, C,  and D options for the user to select from. Use a nested conditional to check if the users answer if correct AND keep score so they can see how well they did at the end of the quiz.

#After each question you need to tell the user if they were right or wrong. what does lebron play ez q

#If the user got the question wrong they should be given an easier question to answer next. 

print("This quiz will be worth your entire grade, and is about sports ")

score = 0

print("when an attacker is behind the defender and receives a pass in soccer, what is the illegal move called? ")
question1 = input('''A: offside
B: foul
C: hold
D: hand ball\n''')

if question1 == "A" or question1 == "offside":
    print("you got this correct!")
    score += 1 
    print("You got", score, "answers correct!")
else:
    print(score)
    print("you got it wrong. You will now receive an easier question. ")

    print("How many points do you get from every basket in basketball? ")
    ez_question1 = input('''    A: 1
    B: 3                   
    C: 2
    D: 4\n''')

    if ez_question1 == "c" or 2:
        score += 1
        print(score)
        print("Nice you got it right! Onto the next question. ")
    else:
        print("aww you still got that wrong. guess we will just move on. ")

print("In volleyball, are you allowed to kick the ball without it being illegal? ")
question2 = input('''A: Yes, as long as you can hold the ball in your feet.
B: No, you cannot kick it.
C: Yes, the ball can touch any part as long as it's not a hold.
D: No, you will be disqualified .\n''')

if question2 == "C" or question1 == "Yes":
    print("You're so right!")
    score += 1
    print(score)