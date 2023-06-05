def max_distance(x, y):
    max = 0
    for i in range(len(x)):
        for j in range(i + 1, len(y)):
            distance = ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) ** 0.5
            if distance > max:
                max = distance
    return max
N = int(input())
x = []
y = []
for i in range(N):
    x_i, y_i = map(int, input().split())
    x.append(x_i)
    y.append(y_i)
print(max_distance(x, y))
