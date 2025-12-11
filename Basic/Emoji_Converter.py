message = input("Message : ")
words = message.split()

Emojies = {
    ":)" : "🙂",
    ":(" : "😔"
}

output=""
for word in words:
    output += Emojies.get(word,word)+"  "

print(output)

