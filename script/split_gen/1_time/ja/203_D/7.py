def get_center_value(matrix, k, x, y):
    center_value = []
    for i in range(k):
        for j in range(k):
            center_value.append(matrix[x+i][y+j])
    center_value.sort()
    return center_value[int((k**2)/2)]
n, k = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
min_center_value = 10**9
for i in range(n-k+1):
    for j in range(n-k+1):
        min_center_value = min(min_center_value, get_center_value(matrix, k, i, j))
print(min_center_value)
