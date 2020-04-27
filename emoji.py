message = input("> ")
words = message.split(' ')

# control + command + space bar
emojis = {
  ":)": "😃",
  ":(": "😌"
}
output = ""

for word in words:
  output += emojis.get(word, word) + " "
print(output)