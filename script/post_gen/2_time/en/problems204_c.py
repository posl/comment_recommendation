Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    A = list(map(lambda x: x - 1, A))
    B = list(map(lambda x: x - 1, B))
    graph = [[] for _ in range(N)]
    for i in range(M):
        graph[A[i]].append(B[i])
    ans = 0
    for i in range(N):
        visited = [False] * N
        visited[i] = True
        stack = [i]
        while stack:
            v = stack.pop()
            for j in graph[v]:
                if not visited[j]:
                    visited[j] = True
                    stack.append(j)
        ans += sum(visited)
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
    ans = 0
    for i in range(N):
        visited = [False] * N
        visited[i] = True
        stack = [i]
        while stack:
            v = stack.pop()
            for nv in G[v]:
                if visited[nv]:
                    continue
                visited[nv] = True
                stack.append(nv)
        ans += sum(visited)
    print(ans)

=======
Suggestion 3

def main():
    N,M = map(int,input().split())
    A = [0]*M
    B = [0]*M
    for i in range(M):
        A[i],B[i] = map(int,input().split())
    print(N*(N-1)-M)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
    ans = 0
    for i in range(N):
        visited = [False]*N
        q = [i]
        while q:
            v = q.pop()
            if not visited[v]:
                visited[v] = True
                for j in G[v]:
                    q.append(j)
        ans += sum(visited)
    print(ans)

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    a = [0]*m
    b = [0]*m
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    
    ans = n*(n-1)
    for i in range(m):
        for j in range(i+1,m):
            if a[i] == a[j] and b[i] == b[j]:
                ans -= 2
            elif a[i] == b[j] and b[i] == a[j]:
                ans -= 2
            elif a[i] == a[j] or a[i] == b[j] or b[i] == a[j] or b[i] == b[j]:
                ans -= 1
    print(ans)
    
main()

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    path = [[0]*n for i in range(n)]
    for i in range(m):
        a,b = map(int,input().split())
        path[a-1][b-1] = 1
    ans = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if path[i][j] == 1:
                for k in range(n):
                    if j == k:
                        continue
                    if path[j][k] == 1:
                        if path[k][i] == 1:
                            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]

    G = [[] for _ in range(N)]
    for a, b in AB:
        G[a - 1].append(b - 1)

    ans = 0
    for i in range(N):
        visited = [False] * N
        visited[i] = True
        q = [i]
        while q:
            v = q.pop()
            for nv in G[v]:
                if not visited[nv]:
                    visited[nv] = True
                    q.append(nv)
        ans += sum(visited)
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    road = []
    for i in range(M):
        A, B = map(int, input().split())
        road.append([A, B])
    if M == 0:
        print(N**2)
        return
    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                ans += 1
                continue
            visited = [0]*(N+1)
            visited[i+1] = 1
            visited[j+1] = 1
            stack = [i+1]
            while len(stack) > 0:
                x = stack.pop()
                for k in range(M):
                    if road[k][0] == x and visited[road[k][1]] == 0:
                        stack.append(road[k][1])
                        visited[road[k][1]] = 1
                    if road[k][1] == x and visited[road[k][0]] == 0:
                        stack.append(road[k][0])
                        visited[road[k][0]] = 1
            ans += sum(visited)
    print(ans)

=======
Suggestion 9

def main():
    import sys
    import numpy as np
    from scipy.sparse.csgraph import floyd_warshall
    input = sys.stdin.readline
    N,M = map(int,input().split())
    A,B = [],[]
    for _ in range(M):
        a,b = map(int,input().split())
        A.append(a-1)
        B.append(b-1)
    A = np.array(A)
    B = np.array(B)
    G = np.zeros((N,N),dtype=np.int64)
    G[A,B] = 1
    G[B,A] = 1
    G = floyd_warshall(G)
    G = np.where(G < float("inf"),1,0)
    print(int(np.sum(G*(N-G-1))))

=======
Suggestion 10

def main():
    # Initialization
    N, M = map(int, input().split())
    # A_i, B_i
    AB = [tuple(map(int, input().split())) for _ in range(M)]

    # Union Find
    par = [i for i in range(N+1)]
    rank = [0 for _ in range(N+1)]

    def find(x):
        if par[x] == x:
            return x
        else:
            par[x] = find(par[x])
            return par[x]

    def unite(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        if rank[x] < rank[y]:
            par[x] = y
        else:
            par[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1

    def same(x, y):
        return find(x) == find(y)

    # Union Find
    for a, b in AB:
        unite(a, b)

    # Count
    cnt = 0
    for i in range(1, N+1):
        if par[i] == i:
            cnt += 1

    # Output
    print(cnt*(cnt-1))
