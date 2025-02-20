def emoji_converter(message):
    words = message.split()

    emoji_dictionary = {
        ":)": "🙂",
        ":(": "😔"
    }

    output = ''

    for word in words:
        output += emoji_dictionary.get(word, word) + ' '
    return output.strip()


message = input("enter message with emoji: ")
print(emoji_converter(message))
