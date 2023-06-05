def solve():
    n, m = map(int, input().split())
    cakes = []
    for _ in range(n):
        x, y, z = map(int, input().split())
        cakes.append((x, y, z))
    ans = 0
    for i in range(1 << 3):
        cakes.sort(key=lambda x: sum(x[j] * (-1 if i >> j & 1 else 1) for j in range(3)))
        ans = max(ans, sum(abs(sum(cakes[i][j] for i in range(m))) for j in range(3)))
    print(ans)
