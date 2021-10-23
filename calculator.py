#--simple calc cause why not


#-extra fancy stuff
import time


#-this will define how the operations work
#adding stuff
def add(x, y):
    return x + y
#subtracting stuff
def subtract(x, y):
    return x - y
#multiplying stuff
def multiply(x, y):
    return x * y
#dividing stuff
def divide(x, y):
    return x / y



#-Client side
print("How would you like to calculate?")
time.sleep(2)
print("Add (+)")
time.sleep(.25)
print("Subtract (-)")
time.sleep(.25)
print("Multiply (*)")
time.sleep(.25)
print("Divide (/)")

#calculation stuff
while True:
    #this will take user input
    time.sleep(.5)
    choice = input("Please enter a (add)+, (subtract)-, (multiply)*, or (divide)/.")

    #this will check if the correct input is provided, then do the math
    if choice in ('+','-','*','/'):
        num1 = float(input("What's your first number?"))
        num2 = float(input("What's your second number?"))
        #adding stuff

        if choice == '+':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '-':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '*':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '/':
            print(num1, "/", num2, "=", divide(num1, num2))

        break
    else:
        print("I can't read that! Decide whether you want to add (+), subtract (-), multiply (*), or divide (/).")

