command = ""

while command != "quit":
  typed_in = input("> ")

  if command == "help":
    print("""
start - to start the car
stop - to stop the car
quit - to exit
"""
    )
  elif command == "start":
    print("Car is started")
  elif command == "stop":
    print("Car is stopped")
  elif command == "stop":
    print("Car is stopped")
  elif command == "quit":
    break
  else:
    print("Sorry I don't understand")
