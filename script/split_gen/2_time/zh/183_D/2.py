def dfs(now, cost, visit):
    global ans
    if cost > K:
        return
    if visit == (1 << N) - 1:
        if cost == K:
            ans += 1
        return
    for i in range(N):
        if visit & (1 << i) == 0:
            dfs(i, cost + T[now][i], visit | (1 << i))
N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]
ans = 0
dfs(0, 0, 1)
print(ans)
