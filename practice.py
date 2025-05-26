# print("hellow world")
# name = input(f'what is your name?')
# age = input(f'how old are you?')
# age = int(age) +1
# print('HAPPY BIRTHDAY')
# print(f'your name is {name} and your age is {age}')
#
# quantity = float(input(f'how much do you like to purchase?'))
# price = float(input(f'how much do you like to purchase?'))
# total = quantity * price
# print(f'you purchased {quantity} of {price} dollars')
# print(total)
#
# price_less_than_35_dollars  = True
# if price_less_than_35_dollars:
#     print('buy ')
# else:
#     print('do not Buy')
# print(type(total))
# print(type(price_less_than_35_dollars))
# print(type(age))
# print(type(name))
# print(type(quantity))
from doctest import Example
from http.client import responses
from math import remainder

# madlib game
# word game where you creat a story
# by filling i the missing words

# adjective1 = input('Enter an adjective(description):')
# noun1 = input('Enter a noun(person, place, thing):')
# adjective2 = input('Enter an adjective(description):')
# verb1 = input('Enter a verb ending with "ing")')
# adjective3 = input('Enter an adjective(description):')
# noun3 = input('Enter a noun(person, place, thing):')
# noun4 = input('Enter a noun(person, place, thing):')
# adjective4 = input('Enter an adjective(description):')
# # output
# print(f'today I went to a {adjective1} Zoo')
# print(f'In an exhibit, I saw a very big {noun1}')
# print(f'{verb1} other animals in the Zoo')
# print(f'But those other animals are so {adjective3}')
# print(f"Especially {noun3} and {noun4}")
# print(f'However the {noun1} was able to {adjective4}')
#
# friends = 5
# friends = friends + 1
# friends = friends - 1
# friends +=3
# friends -=3
# friends *=3
# friends /=3
#friends %=3
#friends = friends *3
#friends = friends **2
# friends **=2
# remander = friends % 2
# print(remander)
import math
from time import process_time_ns

# print(math.pi)
# radius = float(input("Enter radius: "))
# circumference = 2 * math.pi * radius
# area = math.pi * radius ** 2
# print(f'the circumference of the circle is {circumference}')
# print(f'the area of the circle is {area}')
# a = float(input("Enter the side A: "))
# b = float(input("Enter the side B: "))
# c = math.sqrt(pow(a,2) + pow(b,2))
# print(f'the hypotenuse of {a} and {b} is {c}')

##if codition
# age = int(input("Enter your age: "))
# if age <= 18:
#     print("you are not allowed to access this page ")
# elif  age < 0:
#     print("you have not yet been born")
# elif age >= 600:
#     print("are you NOAH")
# else:
#     print("thank you for signing into our page ")

# response = input('would you like to eat some food (Yes or No): ')
# if response == 'Yes':
#     print("have some food please")
# else:
#     print("then I think you can have some water")

# name = input("Enter your name: ")
# if name == "":
#     print("You didn't enter a name")
# else:
#     print("Hello " + name)
# operator = input('enter an operator(+-*/):')
# num1 = float(input('enter first number: '))
# num2 = float(input('enter second number: '))
# # print(num1 + num2)
# if operator == '+':
#     result = num1 + num2
#     print(f'the result is {result}')
# elif operator == '-':
#     result = num1 - num2
#     print(f'the result is {result}')
# elif operator == '*':
#     result = num1 * num2
#     print(f'the result is {result}')
# elif operator == '/':
#     result = num1 / num2
#     print(f'the result is {result}')
# else:
#     print('invalid operator')
## python weight convertor

# weight = float(input("Enter your weight: "))
# units = input("kilograms or pounds? (K or L): ")
# if units == 'k':
#     weight = weight * 2.205
#     units = 'Lbs'
#     print(f"Your weight is {round(weight, 1)} {units}")
# elif units == 'l':
#     weight = weight / 2.205
#     units = 'kgs'
#     print(f"Your weight is {round(weight, 1)} {units}")
# else:
#     print("Invalid input")

# unit = input('Is the temperature in Celsius or Fahrenheit (C/F)?')
# temperature = float(input('What is the temperature? '))
# if unit == 'C':
#     temperature = round(temperature* 9 / 5 + 32,1)
#     print('The temperature in Fahrenheit is', temperature)
# elif unit == 'F':
#     temperature = round((temperature - 32)*5/9,1)
#     print('The temperature in Celsius is', temperature)
# else:
#     print('Invalid unit of measurement')
#
# credit_number = '1234-5674-5768 5987'
# print(credit_number)
# print(credit_number[0])
#print(credit_number[::4])
# print(credit_number[5:9])
# print(credit_number[5:])
#print(credit_number[-1])
# print(credit_number[::3])
# last_four_digits = credit_number[-4:]
# print(f'xxxx-xxxx-xxxx-{last_four_digits}')
# price1 = 3000.65789
# price2 = -36534.46
# price3  = 12456.344
# print(f'price1 is ${price1:.2f}')
# print(f'price2 is ${price2:.3f}')
# print(f'price3 is ${price3:.2f}')
# print(f'price1 is ${price1:10}')
# print(f'price2 is ${price2:10}')
# print(f'price3 is ${price3:10}')
# print(f'price1 is ${price1:+,.2f}')
# print(f'price2 is ${price2:+,.2f}')
# print(f'price3 is ${price3:+,.2f}')
#