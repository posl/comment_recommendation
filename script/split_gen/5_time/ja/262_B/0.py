def solve():
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        a, b = map(int, input().split())
        edges.append((a, b))
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                a = i + 1
                b = j + 1
                c = k + 1
                if (a, b) in edges and (b, c) in edges and (c, a) in edges:
                    ans += 1
    print(ans)
