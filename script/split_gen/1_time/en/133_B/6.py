def is_integer(x):
    if x == int(x):
        return True
    else:
        return False
n, d = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        dis = 0
        for k in range(d):
            dis += (x[i][k] - x[j][k]) ** 2
        if is_integer(dis ** 0.5):
            ans += 1
print(ans)
