Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def get_next_node(node, link, visited):
    for i in range(len(link)):
        if link[i][0] == node and link[i][1] not in visited:
            return link[i][1]
        elif link[i][1] == node and link[i][0] not in visited:
            return link[i][0]
    return 0

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = [0 for _ in range(M)]
    B = [0 for _ in range(M)]
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    print(N, M, A, B)

=======
Suggestion 4

def dfs(now, pre):
    for i in G[now]:
        if i == pre:
            continue
        if vis[i] == 0:
            vis[i] = now
            dfs(i, now)
        else:
            if vis[now] == 0:
                vis[now] = i
                dfs(i, now)

N, M = map(int, input().split())
G = [[] for i in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

vis = [0] * (N+1)
vis[1] = -1
dfs(1, -1)

for i in range(1, N+1):
    if vis[i] == 0:
        print('No')
        exit()
print('Yes')
for i in range(2, N+1):
    print(vis[i])

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A, B = [], []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    print("Yes")
    for i in range(1, N):
        print(A[B.index(i+1)])

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    print(N)
    print(M)
    print(A)
    print(B)

=======
Suggestion 7

def dfs(i):
    global flag
    if flag:
        return
    if visited[i]:
        if visited[i] == 1:
            flag = True
            return
    else:
        visited[i] = 1
        for j in edge[i]:
            dfs(j)
        visited[i] = 2
        ans.append(i)
        return

n,m = map(int,input().split())
edge = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    edge[a].append(b)
visited = [0]*(n+1)
flag = False
ans = []
for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
