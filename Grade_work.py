# Problem 1:
# # #
# # # Create a random number. Print the number.
# # #
# # # Hint:
# # # import random
# # # randomNumber = random.randint(0,9)


import random


def main():
    # problem2()
    problem()

#     problem1()
#
#
# def problem1():
#
#
#     numb1= 0
#     numb2= 9
#     print(random.randint(0,9))
# //////////////////////////////////////////

# Problem 2:
#
# We will keep having this problem until EVERYONE gets it right without help
#
# Create a function that has a loop that quits with ‘q’. If the user doesn't enter 'q', ask them to input another string.

# def problem2():
#     userinput = input("What is your password?\n")
#     endWord = "Q"
#     while (userinput != endWord):
#         if userinput.upper() != endWord:
#             userinput = input("What is your password?\n")
# ///////////////////////////////////////////////////////////////////////////////////////
#
# Problem 3:
#
# Create a function that will loop until the user enters '0'.
# Ask the user to enter a positive integer number.
# Print 0 to that number and ask them again to enter a number until they enter '0'. Repeat.

# def problem3():
while True:
    maxnum=int(input("Enter a postive number."))
    if(maxnum ==0):
        break
    for num in range(0,(maxnum+1)):
        print(num)





# Problem 4:
#
# Create a function that creates a random number. Ask the user to guess the random number.
# Keep letting the user guess until they get it right, then quit.
# If they don't get it right, tell them if their next guess has to be higher or lower.
#

# def problem4():
#     import random
#     mynimba=int(input("Gues a random number."))
#     randomnum= random.randint(0,5)
#     while(mynimba!=randomnum):
#         mynimba=int(input("Guess a random number"))
#









if __name__ == '__main__':
    main()
