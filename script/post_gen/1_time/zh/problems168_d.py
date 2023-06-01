Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def solve():
    pass

=======
Suggestion 3

def dfs(v):
    global flag
    visited[v] = True
    for next_v in G[v]:
        if visited[next_v]:
            continue
        dfs(next_v)
    if flag:
        return
    if v == 1:
        flag = True
        return
    for next_v in G[v]:
        if flag:
            return
        if visited[next_v]:
            continue
        visited[next_v] = True
        ans[next_v] = v
        dfs(next_v)
        visited[next_v] = False
        ans[next_v] = 0

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

flag = False
visited = [False] * (N+1)
ans = [0] * (N+1)
dfs(2)

=======
Suggestion 4

def main():
    N,M = map(int,input().split())
    path = []
    for i in range(M):
        path.append(list(map(int,input().split())))
    print(path)

=======
Suggestion 5

def dfs(x):
    if vis[x]: return
    vis[x] = 1
    for y in G[x]:
        if vis[y]: continue
        dfs(y)
    ans.append(x)

n,m = map(int,input().split())
G = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    G[a].append(b)
vis = [0]*(n+1)
ans = []
for i in range(1,n+1):
    if vis[i]: continue
    dfs(i)
ans = ans[::-1]
vis = [0]*(n+1)
ans2 = []
for i in ans:
    if vis[i]: continue
    ans2.append(i)
    vis[i] = 1
    for j in G[i]:
        vis[j] = 1
print("Yes")
for i in ans2:
    print(i)

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    s = [[0 for i in range(2)] for j in range(m)]
    for i in range(m):
        s[i] = map(int,input().split())
    print(s)

=======
Suggestion 7

def solve():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)
    R = [0] * N
    R[0] = 1
    S = [0]
    while S:
        x = S.pop()
        for y in G[x]:
            if R[y] == 0:
                R[y] = x + 1
                S.append(y)
    print('Yes')
    print('\n'.join(map(str, R[1:])))

solve()
