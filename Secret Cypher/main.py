#ProficiencyTest: Secret Cypher
#Create a program with a function that takes in a users string and uses a shift cypher to turn the string into a secret code.  

input = input("Type anything! ")
shift = ""
def secret_cypher(shift, input):
    for letter in input:
        letter = ord(letter)
        letter += 3
        letter = chr(letter)
        shift += letter
    print(shift)

secret_cypher(shift, input)