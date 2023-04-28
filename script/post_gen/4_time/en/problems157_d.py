Synthesizing 10/10 solutions

=======
Suggestion 1

def readinput():
    n,m,k=list(map(int,input().split()))
    ab=[]
    for _ in range(m):
        a,b=list(map(int,input().split()))
        ab.append((a,b))
    cd=[]
    for _ in range(k):
        c,d=list(map(int,input().split()))
        cd.append((c,d))
    return n,m,k,ab,cd

=======
Suggestion 2

def main():
    N, M, K = map(int, input().split())
    friends = [[] for _ in range(N)]
    blocks = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        friends[A-1].append(B-1)
        friends[B-1].append(A-1)
    for _ in range(K):
        C, D = map(int, input().split())
        blocks[C-1].append(D-1)
        blocks[D-1].append(C-1)
    ans = [0] * N
    for i in range(N):
        ans[i] = len(set(friends[i]) - set(friends[i]) & set(blocks[i])) - 1
    print(' '.join(map(str, ans)))

=======
Suggestion 3

def main():
    N, M, K = map(int, input().split())
    friends = []
    blocks = []
    for _ in range(M):
        friends.append(list(map(int, input().split())))
    for _ in range(K):
        blocks.append(list(map(int, input().split())))
    answer = [0] * N
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j:
                continue
            if [i, j] in friends:
                continue
            if [j, i] in friends:
                continue
            if [i, j] in blocks:
                continue
            if [j, i] in blocks:
                continue
            answer[i - 1] += 1
    print(*answer)

=======
Suggestion 4

def find(parents, x):
    if parents[x] == x:
        return x
    else:
        parents[x] = find(parents, parents[x])
        return parents[x]

=======
Suggestion 5

def main():
    N, M, K = map(int, input().split())
    friend = [0] * N
    block = [0] * N
    for i in range(M):
        A, B = map(int, input().split())
        A -= 1
        B -= 1
        friend[A] += 1
        friend[B] += 1
    for i in range(K):
        C, D = map(int, input().split())
        C -= 1
        D -= 1
        block[C] += 1
        block[D] += 1
    ans = [0] * N
    for i in range(N):
        ans[i] = friend[i] - block[i] - 1
    print(*ans)

=======
Suggestion 6

def find_root(x):
    if par[x] == x:
        return x
    else:
        par[x] = find_root(par[x])
        return par[x]

=======
Suggestion 7

def dfs(start, graph):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

N, M, K = map(int, input().split())
friend = {i: set() for i in range(1, N+1)}
block = {i: set() for i in range(1, N+1)}
for _ in range(M):
    A, B = map(int, input().split())
    friend[A].add(B)
    friend[B].add(A)
for _ in range(K):
    C, D = map(int, input().split())
    block[C].add(D)
    block[D].add(C)

ans = [0] * N
for i in range(1, N+1):
    ans[i-1] = len(dfs(i, friend) - friend[i] - block[i] - {i}) - len(friend[i] & block[i])
print(*ans)

=======
Suggestion 8

def dfs(start, goal):
    visited = [False] * (N+1)
    stack = []
    stack.append(start)
    while stack:
        node = stack.pop()
        if node == goal:
            return True
        if not visited[node]:
            visited[node] = True
            for i in range(len(graph[node])):
                if not visited[graph[node][i]]:
                    stack.append(graph[node][i])
    return False

N, M, K = map(int, input().split())
graph = [[] for i in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(K):
    c, d = map(int, input().split())
    graph[c].append(d)
    graph[d].append(c)
for i in range(1, N+1):
    ans = 0
    for j in range(1, N+1):
        if i == j:
            continue
        if dfs(i, j):
            ans += 1
    print(ans, end = ' ')

=======
Suggestion 9

def dfs(x, y):
    if x in visited:
        return
    visited.add(x)
    if x in friend:
        for z in friend[x]:
            if z == y:
                continue
            dfs(z, y)
    if x in block:
        for z in block[x]:
            if z == y:
                continue
            dfs(z, y)

N, M, K = map(int, input().split())
friend = {}
block = {}
for _ in range(M):
    a, b = map(int, input().split())
    if a not in friend:
        friend[a] = set()
    friend[a].add(b)
    if b not in friend:
        friend[b] = set()
    friend[b].add(a)
for _ in range(K):
    c, d = map(int, input().split())
    if c not in block:
        block[c] = set()
    block[c].add(d)
    if d not in block:
        block[d] = set()
    block[d].add(c)

ans = [0] * N
for i in range(1, N + 1):
    visited = set()
    for j in range(1, N + 1):
        if i == j:
            continue
        dfs(j, i)
    ans[i - 1] = N - len(visited) - 1
print(*ans)

=======
Suggestion 10

def make_set(parent, rank, n):
    parent[n] = n
    rank[n] = 0
