name = input("enter your name: ")
length = len(name)

if (length < 3):
    print("invalid! less than 3 characters!")

elif (length > 50):
    print("invalid! more than 50 characters!")

else:
    print("name looks good.")
