def main():
    import sys
    from collections import deque
    N, M = map(int, input().split())
    if N == 2:
        print(1)
        sys.exit()
    G = [[] for _ in range(N + 1)]
    for i in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    q = deque()
    q.append(1)
    d = [0] * (N + 1)
    d[1] = 1
    while q:
        v = q.popleft()
        for w in G[v]:
            if d[w] == 0:
                d[w] = d[v] + 1
                q.append(w)
    ans = 0
    for v in G[N]:
        if d[v] == d[N] - 1:
            ans += 1
    print(ans % (10 ** 9 + 7))

if __name__ == '__main__':
    main()