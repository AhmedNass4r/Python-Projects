from random import randint
print("Ahmed Nassar")

Choices = ["Rock","Paper","Scissors"]

UserAns = input("Wanna play Rock Paper Scissors? : y/n : ")

UserPoints = 0
CpuPoints = 0

while(UserAns.lower() != "n"):

    if(UserAns.lower() == "y"):
        UserChoice = int(input("1.Rock 2.Paper 3.Scissors : "))
        
        CpuChoice = randint(1,3)
        
        if(Choices[UserChoice - 1] == Choices[CpuChoice - 1]):
            print(f"User choice : {Choices[UserChoice - 1]} , Cpu choice : {Choices[CpuChoice - 1]}")
            print("Draw!")
            UserAns = input("Wanna play Rock Paper Scissors? : y/n : ")
            
        elif(Choices[UserChoice - 1] == "Rock" and Choices[CpuChoice - 1] == "Scissors"):
            print(f"User choice : {Choices[UserChoice - 1]} , Cpu choice : {Choices[CpuChoice - 1]}")
            print("User wins!")
            UserPoints += 1
            print(f"User score : {UserPoints}")
            UserAns = input("Wanna play Rock Paper Scissors? : y/n : ")

        elif(Choices[UserChoice - 1] == "Paper" and Choices[CpuChoice - 1] == "Rock"):
            print(f"User choice : {Choices[UserChoice - 1]} , Cpu choice : {Choices[CpuChoice - 1]}")
            print("User wins!")
            UserPoints += 1
            print(f"User score : {UserPoints}")
            UserAns = input("Wanna play Rock Paper Scissors? : y/n : ")

        elif(Choices[UserChoice - 1] == "Scissors" and Choices[CpuChoice - 1] == "Paper"):
            print(f"User choice : {Choices[UserChoice - 1]} , Cpu choice : {Choices[CpuChoice - 1]}")
            print("User wins!")
            UserPoints += 1
            print(f"User score : {UserPoints}")
            UserAns = input("Wanna play Rock Paper Scissors? : y/n : ")

        else:
            print(f"User choice : {Choices[UserChoice - 1]} , Cpu choice : {Choices[CpuChoice - 1]}")
            print("Cpu wins!")
            CpuPoints += 1
            print(f"Cpu score : {CpuPoints}")
            UserAns = input("Wanna play Rock Paper Scissors? : y/n : ")
    else:
        print("invalid input!")
        UserAns = input("Wanna play Rock Paper Scissors? : y/n : ")
