# temperature = 30
# name = "John"

# if temperature == 30:
#   print("It's a hot day")
# else:
#   print("It not hot")

# print(len(name))

# weight = int(input('What is your weight: '))
# unit = input("(L)bs or (K)g: ")

# if unit == "K" or "k":
#   converted = weight * 2.2
#   print(f"You are {converted} kilos")
# elif unit == "L" or "l":
#   converted = weight / .45
#   print(f"You are {converted} pounds")


# i = 1

# while i <= 5:
#   print(i)
#   i = i + 1
# print("Done")


secret_number = 7
count = 0
max_count = 3

while count < max_count:
  guess = int(input("Guess the number: "))
  count = count + 1
  if guess == secret_number:
    print("You Guessed it")
    break
else:
  print("Sorry ran out of guesses")
