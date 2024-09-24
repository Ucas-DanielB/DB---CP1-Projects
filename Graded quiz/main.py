#Daniel Blanco, Proficiency test: Graded quiz.
#Write a short quiz with at least 5 questions (that have correct and incorrect answers)
#that gives the person a score at the end of the quiz based on how many questions the user got correct. 
#You will need to use an if statement like the example below. 
#if question == correct_answer:
#score += 1

utah = input("Is Utah a state? ")
python = input("Do we use python for our class? ")
ucas = input("Is the school we go to called UCAS? ")
earth = input("Is our planet we live on called earth? ")
italy = input("Is Italy a continent? ")

score = 0

if  utah == "yes" : score += 1
if python == "yes" : score += 1
if ucas == "yes" : score += 1
if earth == "yes" : score += 1
if italy == "no" : score += 1

print(score)