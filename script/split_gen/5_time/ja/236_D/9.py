def xor(a, b):
    return a ^ b
n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        ans = max(ans, xor(a[i][j], a[j][i]))
print(ans)
