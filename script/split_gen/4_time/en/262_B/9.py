def count(a, b, c):
    return (a < b and b < c) or (a > b and b > c)
n, m = map(int, input().split())
graph = [[0] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            ans += count(graph[i][j], graph[j][k], graph[k][i])
print(ans)
