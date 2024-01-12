import random

def input_two_number():
    n = input("Please input minimam number \n")
    m = input("Please input maximum number \n")
    # check if both value is number
    if not (n.isdigit() or m.isdigit()):
        print("error: number can only be input, try again !")
        input_two_number()
    
    # check if both values are not empty
    if n == "" or m == "":
        print("error: minimum number or maximum number should not be empty, try again !")
        input_two_number()
    # check if n is same or smaller than m
    if int(n) > int(m):
        print("error: minimum number should be same or smaller than maximum number, try again !")
        input_two_number()
    
    return int(n), int(m)

def input_answer(n, m, random_number):
    # ask user to guess number 
    answer = input("Please guess random number between " + str(n) + " and " + str(m) + "\n")
    if int(answer) == random_number:
        print("Excellent! Answer is correct")
    else:
        print("Answer is incorrect. Please guess Again!")
        input_answer(n, m, random_number)

def main():
    n, m = input_two_number()
    # create random number
    random_number = random.randint(n, m)
    input_answer(n, m, random_number)

main()
