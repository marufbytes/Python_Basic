numbers = [5, 2, 1, 7, 4]
numbers.append(20)
print(numbers)

numbers = [5, 2, 1, 7, 4]
numbers.insert(0, 10)
print(numbers)

numbers = [5, 2, 1, 7, 4]
numbers.remove(5)
print(numbers)

numbers = [5, 2, 1, 7, 4]
numbers.clear()
print(numbers)

numbers = [5, 2, 1, 7, 4]
numbers.pop()
print(numbers)

numbers = [5, 2, 1, 7, 4]
print(numbers.index(5))

numbers = [5, 2, 1, 7, 4]
print(50 in numbers)

numbers = [5, 2, 5, 5, 1, 7, 4]
print(numbers.count(5))

numbers = [5, 2, 2, 1, 7, 4]
numbers.sort()
print(numbers)

numbers = [5, 2, 2, 1, 7, 4]
numbers.sort()
numbers.reverse()
print(numbers)

numbers = [5, 2, 1, 7, 4]
numbers2 = numbers.copy()
numbers.append(20)
print(numbers)
print(numbers2)
