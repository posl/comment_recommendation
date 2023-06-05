def f(n, m, l):
    ans = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                ans += l[i][j] * l[j][i]
    return ans
n, m = map(int, input().split())
l = [[0 for _ in range(n)] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    l[a-1][b-1] = 1
print(f(n, m, l))
