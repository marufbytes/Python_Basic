matrix = [
    [1,2,4],
    [4,5,6],
    [7,8,9]
]

matrix [1][1]=20

print(matrix[0][0])
print(matrix[1][1])

for row in matrix:
    for item in row:
        print(item)
