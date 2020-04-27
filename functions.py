def greet_user(name, age):
  print(f"Hi {name}")
  print(f"His age is {age}")

greet_user("John", 24)
# # This way can not be in order
# If both, Keyword Arguments must come after Positional Arguments
greet_user(age=18, name="Tim")
