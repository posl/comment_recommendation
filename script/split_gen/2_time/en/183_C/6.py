def dfs(c, t):
    global ans
    if c == n:
        if t == k:
            ans += 1
    else:
        for i in range(n):
            if i != c and not used[i]:
                used[i] = 1
                dfs(c + 1, t + t[c][i])
                used[i] = 0
n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]
ans = 0
used = [0] * n
used[0] = 1
dfs(1, 0)
print(ans)
