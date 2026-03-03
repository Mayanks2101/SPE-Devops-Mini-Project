"""
Scientific Calculator - DevOps Mini Project
Author: Mayank Satapara
Description:
Menu-driven scientific calculator supporting:
1. Square Root
2. Factorial
3. Natural Logarithm
4. Power Function
"""

import math
def display_menu():
    print("\nScientific Calculator")
    print("1. Square Root")
    print("2. Factorial")
    print("3. Natural Logarithm")
    print("4. Power Function")
    print("5. Exit")

def main():
    while True:
        display_menu()
        choice = input("Select an operation (1-5): ")
        
        if choice == '1':
            num = float(input("Enter a number: "))
            if num < 0:
                print("Error: Cannot compute square root of a negative number.")
            else:
                print(f"Square Root of {num} is {math.sqrt(num)}")
        
        elif choice == '2':
            num = int(input("Enter a non-negative integer: "))
            if num < 0:
                print("Error: Factorial is not defined for negative numbers.")
            else:
                print(f"Factorial of {num} is {math.factorial(num)}")
        
        elif choice == '3':
            num = float(input("Enter a positive number: "))
            if num <= 0:
                print("Error: Natural logarithm is only defined for positive numbers.")
            else:
                print(f"Natural Logarithm of {num} is {math.log(num)}")
        
        elif choice == '4':
            base = float(input("Enter the base: "))
            exponent = float(input("Enter the exponent: "))
            print(f"{base} raised to the power of {exponent} is {math.pow(base, exponent)}")
        
        elif choice == '5':
            print("Exiting the calculator.")
            break
        
        else:
            print("Invalid choice. Please select a valid operation.")

if __name__ == "__main__":
    main()