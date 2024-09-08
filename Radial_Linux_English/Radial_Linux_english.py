import math
from fractions import Fraction
import re

def degrees_to_radians_fraction(degrees):
    radians = math.radians(degrees)
    fraction_of_pi = radians / math.pi
    return Fraction(fraction_of_pi).limit_denominator()

def radians_to_degrees_fraction(radians):
    degrees = math.degrees(radians)
    return degrees

def parse_radians_input(user_input):
    match = re.match(r'([+-]?\d*\.?\d*)π(/(\d+))?', user_input)
    if match:
        multiplier = float(match.group(1)) if match.group(1) else 1
        denominator = float(match.group(3)) if match.group(3) else 1
        return multiplier * math.pi / denominator
    else:
        raise ValueError('Invalid input.')

choice = input('Choose the conversion: 1 for degrees to radians, 2 for radians to degrees: ')

if choice == '1':
    degrees = float(input('Enter the degrees: '))
    fraction_of_pi = degrees_to_radians_fraction(degrees)
    numerator, denominator = fraction_of_pi.numerator, fraction_of_pi.denominator

    if numerator == 1 and denominator == 1:
        print(f"{degrees} degrees is π radians.")
    elif numerator == -1 and denominator == 1:
        print(f"{degrees} degrees is -π radians.")
    elif denominator == 1:
        print(f"{degrees} degrees is {numerator}π radians.")
    else:
        print(f"{degrees} degrees is {numerator}π/{denominator} radians.")

elif choice == '2':
    user_input = input('Enter the radians (π): ')
    try:
        radians = parse_radians_input(user_input)
        degrees = radians_to_degrees_fraction(radians)
        print(f"{user_input} radians is {degrees} degrees.")
    except ValueError as e:
        print(e)
else:
    print('Invalid choice.')
