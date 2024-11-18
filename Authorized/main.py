#Write a program that checks if a user is in the the list of authorized users (HINT: you can use the keyword 'in' to check if a value is in a list). 
#And then print out if they are an admin, uesr, or not authorized. (Yes that means you need to set at least 1 admin).

#Authorized users should have at least 8 people on it

special_list = ["1", "2", "3", "4", "5", "6", "7", "8", "0"]

admin_list = ["0"]

question = input("please, give me a number: ")


if question in special_list:
    print("You are authorized!")

else:
    print("HEY! YOU'RE NOT AUTHORIZED SIR")

if question in admin_list:
    print("WOW! An Admin!")