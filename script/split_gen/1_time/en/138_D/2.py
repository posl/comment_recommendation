def main():
    N, Q = map(int, input().split())
    E = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        E[a-1].append(b-1)
        E[b-1].append(a-1)
    P, X = [], []
    for _ in range(Q):
        p, x = map(int, input().split())
        P.append(p-1)
        X.append(x)
    A = [0] * N
    for p, x in zip(P, X):
        A[p] += x
    Q = [0]
    V = [0] * N
    while Q:
        v = Q.pop()
        for u in E[v]:
            if V[u]:
                continue
            V[u] = 1
            A[u] += A[v]
            Q.append(u)
    print(*A)
