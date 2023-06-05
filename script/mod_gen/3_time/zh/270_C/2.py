def dfs(i):
    global ans
    global visited
    global G
    visited[i] = True
    ans.append(i)
    for j in G[i]:
        if visited[j] == False:
            dfs(j)
            ans.append(i)
N,X,Y = map(int,input().split())
U = [0] * (N-1)
V = [0] * (N-1)
G = [[] for _ in range(N+1)]
for i in range(N-1):
    U[i],V[i] = map(int,input().split())
    G[U[i]].append(V[i])
    G[V[i]].append(U[i])
visited = [False] * (N+1)
ans = []
dfs(X)
ans.append(X)
ans = ans[::-1]
ans = ans[ans.index(Y):]
for i in ans:
    print(i,end=' ')
print()

if __name__ == '__main__':
    dfs()