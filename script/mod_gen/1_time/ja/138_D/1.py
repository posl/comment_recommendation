def main():
    N, Q = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        G[a - 1].append(b - 1)
    P = []
    X = []
    for _ in range(Q):
        p, x = map(int, input().split())
        P.append(p - 1)
        X.append(x)
    ans = [0] * N
    for i in range(Q):
        ans[P[i]] += X[i]
    stack = [0]
    while stack:
        u = stack.pop()
        for v in G[u]:
            ans[v] += ans[u]
            stack.append(v)
    print(*ans)

if __name__ == '__main__':
    main()