Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def dfs(x):
    global flag
    if flag:
        return
    if visited[x]:
        return
    visited[x] = True
    for i in range(len(g[x])):
        if g[x][i] == 1:
            dfs(i)
            if flag:
                path[x] = i
                return
    visited[x] = False

=======
Suggestion 3

def dfs(v):
    global ans
    if visited[v]: return
    visited[v] = True
    for u in G[v]:
        if visited[u]: continue
        dfs(u)
    ans.append(v)

N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    A -= 1; B -= 1
    G[A].append(B)
    G[B].append(A)

visited = [False] * N
ans = []
dfs(0)

ans = ans[::-1]
ans = [i + 1 for i in ans]
print("Yes")
print(*ans, sep="\n")

=======
Suggestion 4

def solve():
    pass

=======
Suggestion 5

def solve(N, M, A, B):
    pass

=======
Suggestion 6

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
