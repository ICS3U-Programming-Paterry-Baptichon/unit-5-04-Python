#!/usr/bin/env python3

# Created by Paterry Baptichon
# Created on 2022-05-10 
# this program t has a function that accepts the operation as well as the two decimals
# It asks for 3 parameters: the sign of the operation 
# as a char and the two numbers as floats


def calculate(choice, num1, num2):
    if choice in ('1', '2', '3', '4'):
        if choice == '1':
            print(num1, "+", num2, "=", (num1 + num2))

        elif choice == '2':
            print(num1, "-", num2, "=", (num1 - num2))

        elif choice == '3':
            print(num1, "*", num2, "=", (num1 * num2))

        elif choice == '4':
            print(num1, "÷", num2, "=", (num1 / num2))


def main():
    
    
    print("Select operation.")
    print("1.+")
    print("2.-")
    print("3.*")
    print("4.÷")
# user's operation input
    choice = input("Enter choice(1/2/3/4): ")
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    if choice in ('1', '2', '3', '4'):
    # if the user input isn't valid display invalid input
        try:
            num1_float = float(num1)
            num2_float = float(num2)
        except Exception:
            print("Invalid input")
 # It returns the result of doing the operation on the two numbers.
    calculate(choice, num1_float, num2_float)


if __name__ == "__main__":
    main()


