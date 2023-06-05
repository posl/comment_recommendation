def dfs(now, pre):
    for to in G[now]:
        if to == pre:
            continue
        if ans[to] == 0:
            ans[to] = now
            dfs(to, now)
        else:
            ans[to] = now
            dfs(to, now)
    return
N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
ans = [0]*(N+1)
ans[1] = 1
dfs(1, -1)
print("Yes")
for i in range(2, N+1):
    print(ans[i])

if __name__ == '__main__':
    dfs()