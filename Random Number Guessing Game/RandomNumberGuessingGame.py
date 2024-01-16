from random import *
print("Ahmed Nassar")

RandomNumber = randint(1,10)

UserChoice = input("wanna guess a number (1-10) ? : y/n : ")

while(UserChoice != "n" or UserChoice != "N"):

    try:
        
        if(UserChoice == "y" or UserChoice == "Y"):

            UserGuess = int(input("your guess? : "))

            if(UserGuess == RandomNumber):
                print("You are correct!")
                UserChoice = input("wanna play a again ? : y/n : ")

            elif(UserGuess == RandomNumber+1 or UserGuess == RandomNumber-1):
                print("you are very close!")
                UserGuess = int(input("Guess again! : "))

            elif(UserGuess == RandomNumber+2 or UserGuess == RandomNumber-2):
                print("you are close!")
                UserGuess = int(input("Guess again! : "))

            else:
                print("Not even close!")
                UserGuess = int(input("Guess again! : "))
        else:
            if(UserChoice == "n" or UserChoice =="N"):
                print("ok then bye!")
                break

            else:
                print("invalid choice!")
                UserChoice = input("wanna guess a number (1-10) ? : y/n : ")

    except(ValueError):
        print("please enter a number!")
        UserChoice = input("wanna guess a number (1-10) ? : y/n : ")
