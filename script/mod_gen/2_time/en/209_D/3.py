def main():
    N, Q = map(int, input().split())
    edge = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        edge[a - 1].append(b - 1)
        edge[b - 1].append(a - 1)
    dist = [0] * N
    stack = [0]
    while stack:
        v = stack.pop()
        for u in edge[v]:
            if dist[u] == 0 and u != 0:
                dist[u] = dist[v] + 1
                stack.append(u)
    for _ in range(Q):
        c, d = map(int, input().split())
        if (dist[c - 1] + dist[d - 1]) % 2 == 0:
            print("Town")
        else:
            print("Road")

if __name__ == '__main__':
    main()