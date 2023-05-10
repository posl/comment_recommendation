def dfs(v,p):
    global ans
    ans.append(v)
    for u in G[v]:
        if u != p:
            dfs(u,v)
            ans.append(v)
    return
N,X,Y = map(int,input().split())
X -= 1
Y -= 1
G = [[] for i in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
ans = []
dfs(X,-1)
ans = ans[::-1]
ans.pop()
dfs(Y,-1)
ans = ans[::-1]
ans.pop()
print(*[i+1 for i in ans])

if __name__ == '__main__':
    dfs()