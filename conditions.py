is_hot = False
is_cold = False

# if is_hot:
#   print("it's a hot day")
#   print("Drink plenty of water!")
# elif is_cold:
#   print("It's a cold day")
#   print("Wear warm cloths")
# else:
#   print("enjoy your day")

good_credit = True
high_income = True
criminal_record = False
cost = 1000000
down_payment = 0

# if good_credit:
#   down_payment = (cost * .10)
#   print(down_payment)
# else:
#   down_payment = (cost * .20)
#   print(down_payment)
# print(f"Down Payment: ${down_payment}")

# if good_credit and high_income:
#   print("Eligble for Loan")

# if good_credit or high_income:
#   print("Eligble for Loan")

if good_credit and not criminal_record:
  print("Eligble for Loan")


