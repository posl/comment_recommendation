def dfs(i, a, b, c):
    global ans
    if i == N:
        if min(a, b, c) > 0:
            ans = min(ans, abs(a - A) + abs(b - B) + abs(c - C) - 30)
        return
    dfs(i + 1, a, b, c)
    dfs(i + 1, a + L[i], b, c)
    dfs(i + 1, a, b + L[i], c)
    dfs(i + 1, a, b, c + L[i])
N, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(N)]
ans = 10**9
dfs(0, 0, 0, 0)
print(ans)
