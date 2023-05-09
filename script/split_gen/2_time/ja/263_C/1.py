def dfs(s):
    if len(s) == N:
        print(*s)
        return
    for i in range(s[-1],M+1):
        dfs(s+[i])
N,M = map(int,input().split())
for i in range(1,M+1):
    dfs([i])
