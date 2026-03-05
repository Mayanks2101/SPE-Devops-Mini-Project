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
import logging

logging.basicConfig(
    filename="calculator.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class ScientificCalculator:
    @staticmethod
    def square_root(num):
        if num < 0:
            logging.error("Cannot compute square root of a negative number.")
            raise ValueError("Cannot compute square root of a negative number.")
        result = math.sqrt(num)
        logging.info(f"Square Root of {num} is {result}")
        return result

    @staticmethod
    def factorial(num):
        if num < 0:
            logging.error("Factorial is not defined for negative numbers.")
            raise ValueError("Factorial is not defined for negative numbers.")
        result = math.factorial(num)
        logging.info(f"Factorial of {num} is {result}")
        return result

    @staticmethod
    def natural_log(num):
        if num <= 0:
            logging.error("Natural logarithm is only defined for positive numbers.")
            raise ValueError("Natural logarithm is only defined for positive numbers.")
        result = math.log(num)
        logging.info(f"Natural Logarithm of {num} is {result}")
        return result

    @staticmethod
    def power(base, exponent):
        result = math.pow(base, exponent)
        logging.info(f"{base} raised to the power of {exponent} is {result}")
        return result
    

def display_menu():
    print("\nScientific Calculator")
    print("1. Square Root")
    print("2. Factorial")
    print("3. Natural Logarithm")
    print("4. Power Function")
    print("5. Exit")

def main():
    calculator = ScientificCalculator()
    while True:
        display_menu()
        choice = input("Select an operation (1-5): ")

        try:
            if choice == '1':
                num = float(input("Enter a number: "))
                result = calculator.square_root(num)
                print(f"Square Root of {num} is {result}")

            elif choice == '2':
                num = int(input("Enter a non-negative integer: "))
                result = calculator.factorial(num)
                print(f"Factorial of {num} is {result}")

            elif choice == '3':
                num = float(input("Enter a positive number: "))
                result = calculator.natural_log(num)
                print(f"Natural Logarithm of {num} is {result}")

            elif choice == '4':
                base = float(input("Enter the base: "))
                exponent = float(input("Enter the exponent: "))
                result = calculator.power(base, exponent)
                print(f"{base} raised to the power of {exponent} is {result}")

            elif choice == '5':
                print("Exiting the calculator.")
                break

            else:
                print("Invalid choice. Please select a valid operation.")

        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()