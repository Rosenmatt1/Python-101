import functions
import utils
from functions import greet_user

import math
# Google search python 3 math module

price = 10

# variable must be lower case - booleans must be capitalized
is_published = False



# birth_year = input('Birth year: ')
# age = 2019 - birth_year
# # print(age)
# print(type(birth_year))

# weight = input('What is your weight: ')
# converted = weight * .45
# print(converted)

# message = ''' 
# This is a mutli line string

# From John
# '''

course = 'Python for Beginners'
# This returns 0,1 and 2 index
# print(course[0:3])
# print(course[1:-1])

# string formatting
first = 'John'
last =  'Smith'
message = first + last + ' is a coder'
message = first +  ' [' + last + '] is a coder'
# msg = f'{first} [{last}] is a coder'
# print(message)

course = "This is the Pourse"
# print(len(course))
# print(course.upper())
# print(course.find('P'))
# print(course.replace('P', 'C'))
# print(course.replace('P', 'Best C'))
print('Pourse' in course)


# Returns division without decimal 
print(10 // 3)
# modulas operator returns remainder 
print(10 % 3)
# 10 to the power of 3
print(10 ** 3)
# Rounds Up
x = 2.9
print(round(x))

numbers5 = [7, 16, 3, 1, 11]
numbers5.append(20)

numbers5.insert(1,33)
print("index", numbers5.index(3))

# numbersNew = numbers5.copy()
# print(numbersNew)

print(numbers5)

greet_user("John", 18)
functions.greet_user("Sally", 20)

max = utils.find_max([7,10,11,2,9,6])
print(max)








