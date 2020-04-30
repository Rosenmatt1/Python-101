from pathlib import Path

# path = Path("ecommerce")
# print(path.exists("ecommerce"))

path1 = Path("newFolder")
# path1.mkdir()
# path1.rmdir()

path = Path()
# print(path.glob(*.*))
# print(path.glob(*.py))
# print(path.glob(*.xls))

for file in path.glob('*.*'):
  print(file)
