def get_ints(): return map(int, input().split())
n, d = get_ints()
x = [list(get_ints()) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(i+1, n):
        dist = 0
        for k in range(d):
            dist += (x[i][k] - x[j][k])**2
        if int(dist**0.5) == dist**0.5:
            ans += 1
print(ans)
