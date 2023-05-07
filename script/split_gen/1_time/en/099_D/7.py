def solve():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            for k in range(3):
                if i == k or j == k:
                    continue
                cost = [[0] * C for _ in range(3)]
                for x in range(N):
                    for y in range(N):
                        cost[(x + y) % 3][c[x][y] - 1] += D[c[x][y] - 1][(i + j + k) % C]
                ans = min(ans, sum(min(cost[i]) for i in range(3)))
    print(ans)
