def dfs(N,M,now):
    if len(now)==N:
        print(*now)
        return
    for i in range(now[-1]+1,M+1):
        dfs(N,M,now+[i])
N,M=map(int,input().split())
for i in range(1,M+1):
    dfs(N,M,[i])
