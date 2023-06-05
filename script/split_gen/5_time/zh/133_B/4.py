def distance(x, y):
    dist = 0
    for i in range(len(x)):
        dist += (x[i] - y[i]) ** 2
    return dist ** 0.5
N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        if distance(X[i], X[j]).is_integer():
            ans += 1
print(ans)
