# class Point:
#   def __init__(self, x, y):
#     self.x = x
#     self.y = y
  
#   def move(self):
#     print("move")
#   def draw(self):
#     print("draw")

# point1  = Point(10, 20)
# # point1.q = 10
# # print(point1.q)

# print(point1.x)
# point1.draw()

class Person:
  def __init__(self, name):
    self.name = name

  def talk(self):
    print(f"The user name is {self.name}")

user1 = Person("John")
print(user1.name)
user1.talk()
