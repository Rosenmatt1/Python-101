# tuples are immutable
coordinates = (1, 2, 3)

# unpacks list of tuple into variables
x, y, z = coordinates

customer = {
  "name": "John Smith",
  "age": 30,
  "is_verified": True
}

customer["name"] = "Jack Dong"
customer["birthdate"] = "Jan 1 1980"

# print(customer["name"])
print(customer.get("name"))
print(customer.get("birthdate"))
