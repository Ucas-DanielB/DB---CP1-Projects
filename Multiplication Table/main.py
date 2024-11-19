#INSTRUCTIONS:
#Write a program that asks a user what number they would like multiples of, then print out that multiples of that number (0-12 just like on a multiplication table. (Your program must use a for loop)

#Bonus!
#Set up your for loop to print out multiples of all the numbers just like a real multiplication table 

#(I recommend separating items in the row by |'s and including and styling it to be easy to read)

user_input = int(input("What number do you want multiples of? "))

for multiple in range(13):
    
    print(user_input * multiple)