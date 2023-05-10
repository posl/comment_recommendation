def check(x, y, n):
    for i in range(n):
        if (x>>i)&1:
            for j in range(len(y[i])):
                if (y[i][j]>>i)&1 != (x>>i)&1:
                    return False
    return True
n = int(input())
a = []
y = []
for i in range(n):
    a.append(int(input()))
    y.append([])
    for j in range(a[i]):
        x, y[i][j] = map(int, input().split())
        y[i][j] -= 1
ans = 0
for i in range(1<<n):
    if check(i, y, n):
        ans = max(ans, bin(i).count('1'))
print(ans)
