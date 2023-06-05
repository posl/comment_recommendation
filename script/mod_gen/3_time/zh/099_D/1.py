def solve():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    C = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(N)]
    mod = [[0] * C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            mod[(i + j) % 3][C[i][j]] += 1
    res = float("inf")
    for c0 in range(C):
        for c1 in range(C):
            if c0 == c1:
                continue
            for c2 in range(C):
                if c0 == c2 or c1 == c2:
                    continue
                tmp = 0
                for c in range(C):
                    tmp += D[c][c0] * mod[0][c]
                    tmp += D[c][c1] * mod[1][c]
                    tmp += D[c][c2] * mod[2][c]
                res = min(res, tmp)
    print(res)

if __name__ == '__main__':
    solve()