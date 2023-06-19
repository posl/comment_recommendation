def dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
N = int(input())
X = []
Y = []
for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
max_dist = 0
for i in range(N):
    for j in range(i + 1, N):
        max_dist = max(max_dist, dist(X[i], Y[i], X[j], Y[j]))
print(max_dist)
