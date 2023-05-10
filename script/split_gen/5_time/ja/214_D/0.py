def solve():
    N = int(input())
    edges = []
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))
    edges.sort()
    ans = 0
    for w, u, v in edges:
        ans += w * min(u, v) * (N - max(u, v) + 1)
    print(ans)
