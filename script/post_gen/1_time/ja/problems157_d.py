Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, K = map(int, input().split())
    A = []
    B = []
    C = []
    D = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for _ in range(K):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)
    #print(N, M, K)
    #print(A)
    #print(B)
    #print(C)
    #print(D)
    #print(len(A))
    #print(len(B))
    #print(len(C))
    #print(len(D))
    #print(A[0])
    #print(B[0])
    #print(C[0])
    #print(D[0])
    #print(A[0] == B[0])
    #print(C[0] == D[0])
    #print(A[0] == C[0])
    #print(A[0] == D[0])
    #print(B[0] == C[0])
    #print(B[0] == D[0])
    #print(A[0] == C[0])
    #print(A[0] == D[0])
    #print(B[0] == C[0])
    #print(B[0] == D[0])
    #print(A[0] == D[0])
    #print(B[0] == C[0])
    #print(A[0] == B[0])
    #print(C[0] == D[0])
    #print(A[0] == C[0])
    #print(A[0] == D[0])
    #print(B[0] == C[0])
    #print(B[0] == D[0])
    #print(A[0] == C[0])
    #print(A[0] == D[0])
    #print(B[0] == C[0])
    #print(B[0] == D[0])
    #print(A[0] == D[0])
    #print(B[0] == C[0])
    #print(A[0] == B[0])
    #print(C[0] == D[0])
    #print(A[0] == C[0])
    #print(A[

=======
Suggestion 2

def main():
    N, M, K = map(int, input().split())
    friend = [set() for _ in range(N)]
    block = [set() for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        A -= 1
        B -= 1
        friend[A].add(B)
        friend[B].add(A)
    for _ in range(K):
        C, D = map(int, input().split())
        C -= 1
        D -= 1
        block[C].add(D)
        block[D].add(C)

    ans = [0] * N
    for i in range(N):
        ans[i] = len(friend[i] - block[i] - set([i])) - 1

    print(*ans)

=======
Suggestion 3

def dfs(v, c):
    color[v] = c
    for i in graph[v]:
        if color[i] == c:
            return False
        if color[i] == 0 and not dfs(i, -c):
            return False
    return True

n, m, k = map(int, input().split())
graph = [[] for _ in range(n)]
color = [0] * n

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    if color[i] == 0:
        if not dfs(i, 1):
            print('No')
            exit()

print('Yes')

=======
Suggestion 4

def main():
    n, m, k = map(int, input().split())
    a = [0] * (n + 1)
    b = [0] * (n + 1)
    c = [0] * (n + 1)
    d = [0] * (n + 1)
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    for i in range(k):
        c[i], d[i] = map(int, input().split())
    for i in range(m):
        a[i] -= 1
        b[i] -= 1
    for i in range(k):
        c[i] -= 1
        d[i] -= 1
    uf = UnionFind(n)
    for i in range(m):
        uf.union(a[i], b[i])
    for i in range(k):
        uf.union(c[i], d[i])
    ans = [0] * n
    for i in range(n):
        ans[i] = uf.size(i) - uf.size_tree(i) - 1
    print(*ans)

=======
Suggestion 5

def main():
    n,m,k = map(int,input().split())
    f = [set() for _ in range(n)]
    b = [set() for _ in range(n)]
    for _ in range(m):
        a,b = map(int,input().split())
        a,b = a-1,b-1
        f[a].add(b)
        f[b].add(a)
    for _ in range(k):
        c,d = map(int,input().split())
        c,d = c-1,d-1
        b[c].add(d)
        b[d].add(c)
    ans = [0]*n
    for i in range(n):
        ans[i] = len(f[i] - b[i] - {i}) - 1
    print(*ans)

=======
Suggestion 6

def solve():
    n,m,k=map(int,input().split())
    friend=set()
    block=set()
    for _ in range(m):
        a,b=map(int,input().split())
        friend.add((a,b))
        friend.add((b,a))
    for _ in range(k):
        c,d=map(int,input().split())
        block.add((c,d))
        block.add((d,c))
    ans=[0]*n
    for i in range(n):
        for j in range(1,n+1):
            if i+1==j:
                continue
            if (i+1,j) in block:
                continue
            if (i+1,j) in friend:
                continue
            if (j,i+1) in friend:
                continue
            ans[i]+=1
    print(*ans)

=======
Suggestion 7

def dfs(v, c):
    global color
    color[v] = c
    for i in range(len(graph[v])):
        if color[graph[v][i]] == c:
            return False
        if color[graph[v][i]] == 0 and not dfs(graph[v][i], -c):
            return False
    return True

=======
Suggestion 8

def dfs(start, end, graph, visited):
    visited[start] = True
    if start == end:
        return True
    for node in graph[start]:
        if not visited[node]:
            if dfs(node, end, graph, visited):
                return True
    return False

=======
Suggestion 9

def dfs(u, color):
    color[u] = 1
    for v in edge[u]:
        if color[v] == 0:
            dfs(v, color)

=======
Suggestion 10

def dfs(graph, start, goal):
    stack = [start]
    paths = []
    while stack:
        v = stack.pop()
        if v not in paths:
            paths.append(v)
            stack += graph[v]
    return paths

N, M, K = map(int, input().split())
friends = [[] for _ in range(N)]
blocks = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    friends[a-1].append(b)
    friends[b-1].append(a)
for _ in range(K):
    c, d = map(int, input().split())
    blocks[c-1].append(d)
    blocks[d-1].append(c)
ans = [0] * N
for i in range(N):
    ans[i] = len(set(dfs(friends, i+1, 0)) & set(dfs(blocks, i+1, 0))) - 1 - len(friends[i])
print(*ans)
