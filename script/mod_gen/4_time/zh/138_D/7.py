def dfs(v):
    global ans
    ans[v] += x
    for i in range(len(child[v])):
        dfs(child[v][i])
    return
N,Q = map(int,input().split())
child = [[] for i in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    child[a-1].append(b-1)
ans = [0] * N
for i in range(Q):
    p,x = map(int,input().split())
    dfs(p-1)
print(*ans)

if __name__ == '__main__':
    dfs()