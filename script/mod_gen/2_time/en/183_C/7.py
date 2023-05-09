def dfs(v, d, t):
    global ans, n, k, t
    if d == n and v == 0:
        if t == k:
            ans += 1
    else:
        for i in range(n):
            if i != v and not used[i]:
                used[i] = True
                dfs(i, d+1, t+tt[v][i])
                used[i] = False
n, k = map(int, input().split())
tt = [list(map(int, input().split())) for _ in range(n)]
ans = 0
used = [False]*n
used[0] = True
dfs(0, 1, 0)
print(ans)

if __name__ == '__main__':
    dfs()