# temperature = 30
# name = "John"

# if temperature == 30:
#   print("It's a hot day")
# else:
#   print("It not hot")

# print(len(name))

weight = int(input('What is your weight: '))
unit = input("(L)bs or (K)g: ")

if unit == "K" or "k":
  converted = weight * 2.2
  print(f"You are {converted} kilos")
elif unit == "L" or "l":
  converted = weight / .45
  print(f"You are {converted} pounds")
