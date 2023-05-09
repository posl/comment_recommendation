def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    sys.setrecursionlimit(10**8)
    N,Q = map(int,input().split())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a,b = map(int,input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    P = [0]*N
    D = [0]*N
    Q = deque([0])
    while Q:
        v = Q.popleft()
        for u in G[v]:
            if D[u] == 0:
                D[u] = D[v] + 1
                P[u] = v
                Q.append(u)
    A = [0]*N
    for _ in range(Q):
        p,x = map(int,input().split())
        p -= 1
        A[p] += x
        if p != 0:
            A[P[p]] -= x
    Q = deque([0])
    while Q:
        v = Q.popleft()
        for u in G[v]:
            if D[u] > D[v]:
                A[u] += A[v]
                Q.append(u)
    print(*A)
