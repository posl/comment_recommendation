def dfs(v, p):
    for i in G[v]:
        if i == p: continue
        if not seen[i]:
            seen[i] = True
            dfs(i, v)
        else:
            print("Yes")
            print(v)
            print(i)
            exit()
N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)
seen = [False] * (N+1)
seen[1] = True
dfs(1, 0)
print("No")
