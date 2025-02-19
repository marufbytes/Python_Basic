list = [1,2,3,4,5,5,6,6,6,6,7,8]
print(list)
unique = []

for digits in list:
    if digits not in unique:
        unique.append(digits)

print(unique)
