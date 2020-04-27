message = input("> ")

# control + command + space bar
emojis = {
    ":)": "😃",
    ":(": "😌"
}

def run_emoji(message, emojis):
  output = ""
  words = message.split(' ')
  for word in words:
    output += emojis.get(word, word) + " "
  return output


result = run_emoji(message, emojis)
print(result)
