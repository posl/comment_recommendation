Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    U = []
    V = []
    for i in range(M):
        u, v = map(int, input().split())
        U.append(u)
        V.append(v)
    ans = 0
    for i in range(M):
        for j in range(i+1, M):
            if U[i] == U[j] or U[i] == V[j] or V[i] == U[j] or V[i] == V[j]:
                continue
            for k in range(j+1, M):
                if U[i] == U[k] or U[i] == V[k] or V[i] == U[k] or V[i] == V[k]:
                    continue
                if U[i] == U[j] or U[i] == V[j] or V[i] == U[j] or V[i] == V[j]:
                    continue
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    U = []
    V = []
    for i in range(M):
        u, v = map(int, input().split())
        U.append(u)
        V.append(v)

    #print(U)
    #print(V)

    ans = 0
    for i in range(M):
        u = U[i]
        v = V[i]
        u_set = set()
        v_set = set()
        for j in range(M):
            if i == j:
                continue
            if U[j] == u:
                u_set.add(V[j])
            if V[j] == u:
                u_set.add(U[j])
            if U[j] == v:
                v_set.add(V[j])
            if V[j] == v:
                v_set.add(U[j])
        #print(u_set)
        #print(v_set)
        ans += len(u_set & v_set)
    print(ans//3)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)

    answer = 0
    for i in range(N):
        for v in G[i]:
            for w in G[v]:
                if w in G[i]:
                    answer += 1
    print(answer // 6)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    ans = 0
    for i in range(n):
        for j in graph[i]:
            for k in graph[j]:
                if i == k:
                    ans += 1
    print(ans // 6)

=======
Suggestion 5

def solve():
    n,m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        a,b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)
    
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if j in g[i]:
                continue
            for k in range(j+1,n):
                if k in g[i] or k in g[j]:
                    continue
                ans += 1
    print(ans)

=======
Suggestion 6

def comb(n, r):
    if n == r:
        return 1
    elif r == 1:
        return n
    else:
        return comb(n-1, r) + comb(n-1, r-1)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    ans = 0
    for i in range(M):
        for j in range(i + 1, M):
            a, b = edges[i]
            c, d = edges[j]
            if len({a, b, c, d}) == 4:
                if (a, b) in edges and (b, c) in edges and (c, a) in edges:
                    ans += 1
    print(ans)

=======
Suggestion 8

def comb(n,r):
    if n == 0 or r == 0:
        return 1
    if n < r:
        return 0
    return comb(n-1,r-1) + comb(n-1,r)

=======
Suggestion 9

def main():
    n,m = map(int, input().split())
    edge = []
    for i in range(m):
        u,v = map(int, input().split())
        edge.append((u,v))
    #print(edge)
    cnt = 0
    for i in range(m):
        for j in range(i+1, m):
            #print(i,j)
            u1,v1 = edge[i]
            u2,v2 = edge[j]
            if u1 == u2 or u1 == v2 or v1 == u2 or v1 == v2:
                #print(u1,v1,u2,v2)
                cnt += 1
    print(cnt)

=======
Suggestion 10

def check(a,b,c):
    if a < b < c:
        return True
    else:
        return False
