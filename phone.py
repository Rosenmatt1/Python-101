phone = input("phone: ")

numbers = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}

# print(phone)
output = ""

for digit in phone:
  output += numbers.get(digit, "!") + " "
print(output)
