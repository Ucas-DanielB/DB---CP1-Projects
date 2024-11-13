#Write a short program that allows a user to create a shopping list by adding and removing items from the list. You will want to connect this to functions that handle adding and removing items from the list. And print the list after each change.

#Since you don't know loops and conditionals yet use the code below to have your code run more than once. 


food = []
def add():
    object = input("What do you want to add? ")
    food.append(object)
    print(food)
    
def remove():
    object = input("What do you want to remove? ")
    food.remove(object)
    print(food)

while True:

    action = input("""What would you like to do?

                                  Enter 1 to add item

                                  Enter 2 to remove item

                                  Enter 3 to leave the list:\n""")
    

    if action =="1":

        add()

    elif action =="2":

        remove()

    else:

        print("Have a nice day! here is your list! ", food)


        break