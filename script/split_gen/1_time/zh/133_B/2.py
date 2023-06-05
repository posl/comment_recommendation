def get_distance(x, y):
    distance = 0
    for i in range(len(x)):
        distance += (x[i] - y[i]) ** 2
    return distance
N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]
count = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        distance = get_distance(X[i], X[j])
        if (distance ** 0.5).is_integer():
            count += 1
print(count)
