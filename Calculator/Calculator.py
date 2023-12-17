print("By Ahmed Nassar") #Owner -> my github : https://github.com/AhmedNass4r

print("\tMENU") #MENU

#list that contains our options
Options = ["1.Addition","2.Subtraction","3.Multiplication","4.Division","5.Remainder","6.EXIT"]

#a list for input validation
NumList = [1,2,3,4,5,6]

#setting user input to 0
UserIn = 0

#while the user's choice is not 6.EXIT
while(UserIn !=6):

    #printing the MENU for the user
    for i in(Options):
        print(i)
    
    #taking the user's input
    UserIn = int(input("pick an option : "))

    #1 for Addition
    if(UserIn == 1):
        print("you chose Addition")
        num1 = float(input("enter the first number : "))
        num2 = float(input("enter the second number : "))
        add = num1 + num2
        print(f"{num1} + {num2} = {add}")
        
    #2 for Subtraction
    elif(UserIn == 2):
        print("you chose Subtraction")
        num1 = float(input("enter the first number : "))
        num2 = float(input("enter the second number : "))
        sub = num1 - num2
        print(f"{num1} - {num2} = {sub}")
    
    #3 for Multiplication
    elif(UserIn == 3):
        print("you chose Multiplication")
        num1 = float(input("enter the first number : "))
        num2 = float(input("enter the second number : "))
        prod = num1 * num2
        print(f"{num1} X {num2} = {prod}")
        
    #4 for Division
    elif(UserIn == 4):
        print("you chose Division")
        num1 = float(input("enter the first number : "))
        num2 = float(input("enter the second number : "))
        div = num1 / num2
        print(f"{num1} / {num2} =",round(div,2))
        
    #5 for Remainder
    elif(UserIn == 5):
        print("you chose to get the Remainder")
        num1 = float(input("enter the first number : "))
        num2 = float(input("enter the second number : "))
        rem = num1 % num2
        print(f"{num1} mod {num2} = {rem}")
        
    #6 for EXIT
    elif(UserIn == 6):
        print("the program will now EXIT")
        print("DONE!")
        break

    #input validating
    else:
        while(UserIn not in NumList):
            print("invalid input!")
            UserIn = int(input("pick an option : "))
