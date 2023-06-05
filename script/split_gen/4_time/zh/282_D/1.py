def solve():
    n, m = map(int, input().split())
    d = [0] * n
    for _ in range(m):
        u, v = map(int, input().split())
        d[u - 1] += 1
        d[v - 1] += 1
    print(sum(i == 1 for i in d))
