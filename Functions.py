def decor():
    print("="*89,"\n"," "*40,"WELCOME","\n\n","*"*89,"\n\n",end = "")
def calculator ():
    print("1. Addition","2.Subtraction","3.Multiplication","4.Division","5.Out",sep = "\n")    

    choice = int() 
    while True:
        choice = int(input("Enter the number to perform action : "))
        if (choice == 1):
            # def add(num1, num2):
                while True :
                    try:
                        num1 = int(input("Enter the first number : "))
                        num2 = int(input("Enter the second number to add : "))
                        print(f"The sum of {num1} & {num2} is {num1+num2}")
                        print("\n"," * "*40)
                        break
                    except ValueError:
                        print("Enter Numbers only")
                        print("\n"," * "*40)

        elif (choice == 2):
            # def subtract(num1, num2):
                while True :
                    try:
                        num1 = int(input("Enter the first number : "))
                        num2 = int(input("Enter the second number to subtract : "))
                        print(f"The sum of {num1} & {num2} is {num1-num2}")
                        print("\n"," * "*40)
                        break
                    except ValueError:
                        print("Enter Numbers only")
                        print("\n"," * "*40)
        elif (choice == 3): 
            # def multiply(num1, num2):
                while True :
                    try:
                        num1 = int(input("Enter the first number : "))
                        num2 = int(input("Enter the second number to multiply : "))
                        print(f"The sum of {num1} & {num2} is {num1*num2}")
                        print("\n"," * "*40)
                        break
                    except ValueError:
                        print("Enter Numbers only")
                        print("\n"," * "*40)
        elif (choice == 4):
            # def divide(num1, num2):
                while True :
                    try:
                        num1 = int(input("Enter the first number : "))
                        num2 = int(input("Enter the second number to divide : "))
                        print(f"The sum of {num1} & {num2} is {num1/num2}")
                        print("\n"," * "*40)
                        break
                    except ValueError:
                        print("Enter Numbers only")
                        print("\n"," * "*40)
                    except ZeroDivisionError:
                        print("Can't divide by 0")
                        print("\n"," * "*40)
        elif (choice == 5):
             print("--- Thanks for using ---")
             break
        else :
            print("Something wrong")      

decor()
calculator()