def euclidean_distance(x, y):
    return sum([(x_i - y_i)**2 for x_i, y_i in zip(x, y)])**0.5
n, d = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if euclidean_distance(x[i], x[j]).is_integer():
            ans += 1
print(ans)
