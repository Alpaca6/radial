import math
from fractions import Fraction
import re

def graden_naar_radialen_fraction(graden):
    radians = math.radians(graden)
    fraction_of_pi = radians / math.pi
    return Fraction(fraction_of_pi).limit_denominator()

def radialen_naar_graden_fraction(radialen):
    degrees = math.degrees(radialen)
    return degrees

def parse_radialen_input(user_input):
    
    match = re.match(r'([+-]?\d*\.?\d*)π(/(\d+))?', user_input)
    if match:
        multiplier = float(match.group(1)) if match.group(1) else 1
        denominator = float(match.group(3)) if match.group(3) else 1
        return multiplier * math.pi / denominator
    else:
        raise ValueError('Ongeldige invoer.')

keuze = input('Kies de conversie: 1 voor graden naar radialen, 2 voor radialen naar graden: ')

if keuze == '1':
    graden = float(input('Voer de graden in: '))
    fraction_of_pi = graden_naar_radialen_fraction(graden)
    numerator, denominator = fraction_of_pi.numerator, fraction_of_pi.denominator

    if numerator == 1 and denominator == 1:
        print(f"{graden} graden is π radialen.")
    elif numerator == -1 and denominator == 1:
        print(f"{graden} graden is -π radialen.")
    elif denominator == 1:
        print(f"{graden} graden is {numerator}π radialen.")
    else:
        print(f"{graden} graden is {numerator}π/{denominator} radialen.")

elif keuze == '2':
    user_input = input('Voer de radialen in (π): ')
    try:
        radialen = parse_radialen_input(user_input)
        graden = radialen_naar_graden_fraction(radialen)
        print(f"{user_input} radialen is {graden} graden.")
    except ValueError as e:
        print(e)
else:
    print('Ongeldige keuze.')
