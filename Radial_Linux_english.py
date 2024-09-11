import math
from fractions import Fraction
import re

# Global variable to store conversion history
history = []

# Function to convert degrees to radians in fraction of π
def degrees_to_radians_fraction(degrees):
    radians = math.radians(degrees)
    fraction_of_pi = radians / math.pi
    return Fraction(fraction_of_pi).limit_denominator()

# Function to convert radians to degrees
def radians_to_degrees_fraction(radians):
    degrees = math.degrees(radians)
    return degrees

# Function to parse input for degrees
def parse_degrees_input(degrees_input):
    degrees_input = degrees_input.replace(',', '.')  # normalize decimal separator
    match = re.match(r'^([+-]?\d+)°?\s*(\d+)?\'?\s*(\d+)?"?$', degrees_input)
    if match:
        degrees = float(match.group(1))
        minutes = float(match.group(2)) if match.group(2) else 0
        seconds = float(match.group(3)) if match.group(3) else 0
        return degrees + minutes / 60 + seconds / 3600
    else:
        raise ValueError("Invalid input format. Please use the format: degrees (°) minutes (') seconds (\").")

# Function to parse input for radians
def parse_radians_input(radians_input):
    match = re.match(r'([+-]?\d*\.?\d*)π(/(\d+))?', radians_input)
    if match:
        multiplier = float(match.group(1)) if match.group(1) else 1
        denominator = float(match.group(3)) if match.group(3) else 1
        return multiplier * math.pi / denominator
    else:
        raise ValueError('Invalid input. Use a multiplier for π.')

# Function to add conversions to history
def add_to_history(conversion_type, user_input, result):
    if len(history) >= 10:
        history.pop(0)
    history.append((conversion_type, user_input, result))

# Function to show conversion history
def show_history(language):
    if len(history) == 0:
        print("\nNo history yet.")
    else:
        print("\nConversion History:")
        for i, (conversion_type, user_input, result) in enumerate(history, start=1):
            print(f"{i}. Type: {conversion_type}, Input: {user_input}, Output: {result}")
    input("Press Enter to return to the menu.")

# Function to start the program
def start_program():
    language = choose_language()
    
    while True:
        print("\nChoose the conversion:")
        print("1. Degrees to Radians")
        print("2. Radians to Degrees")
        print("3. View History")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            
            degrees_input = input('Enter the degrees (° ’ “): ')
            print(f"Degrees input received: {degrees_input}")
            try:
                degrees = parse_degrees_input(degrees_input)
                fraction_of_pi = degrees_to_radians_fraction(degrees)
                numerator, denominator = fraction_of_pi.numerator, fraction_of_pi.denominator
                if numerator == 1 and denominator == 1:
                    result = f"{degrees} degrees is π radians."
                elif numerator == -1 and denominator == 1:
                    result = f"{degrees} degrees is -π radians."
                elif denominator == 1:
                    result = f"{degrees} degrees is {numerator}π radians."
                else:
                    result = f"{degrees} degrees is {numerator}π/{denominator} radians."

                print(result)
                add_to_history("Degrees to Radians", degrees_input, result)
            except ValueError as e:
                print(e)

        elif choice == '2':
            
            radians_input = input('Enter the radians (π): ')
            print(f"Radians input received: {radians_input}")
            try:
                radians = parse_radians_input(radians_input)
                degrees = radians_to_degrees_fraction(radians)
                result = f"{radians_input} radians is {degrees} degrees."
                print(result)
                add_to_history("Radians to Degrees", radians_input, result)
            except ValueError as e:
                print(e)

        elif choice == '3':
            show_history(language)

        elif choice == '4':
            print("Exiting the program.")
            return

# Function to choose language
def choose_language():
    while True:
        print("\nChoose your language:")
        print("1. English")
        print("2. Dutch")
        print("3. French")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            return 'english'
        elif choice == '2':
            return 'dutch'
        elif choice == '3':
            return 'french'
        else:
            print("Invalid choice. Please choose again.")

# Start the program
start_program()
