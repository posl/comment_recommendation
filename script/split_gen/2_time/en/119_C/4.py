def dfs(i, a, b, c):
    global ans
    if i == N:
        if min(a, b, c) > 0:
            ans = min(ans, abs(a - A) + abs(b - B) + abs(c - C) - 30)
        return
    dfs(i + 1, a, b, c)
    dfs(i + 1, a + l[i], b, c) + 10
    dfs(i + 1, a, b + l[i], c) + 10
    dfs(i + 1, a, b, c + l[i]) + 10
N, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(N)]
ans = 10 ** 9
dfs(0, 0, 0, 0)
print(ans)
Thank you for your contribution!
Thank you for your contribution!
Thank you for your contribution!
Thank you for your contribution
