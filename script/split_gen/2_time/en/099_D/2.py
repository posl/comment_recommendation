def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    for i in range(C):
        for j in range(C):
            D[i][j] = min(D[i][j], D[i][0] + D[0][j])
    ans = 10 ** 18
    for i in range(C):
        for j in range(C):
            if i == j:
                continue
            for k in range(C):
                if i == k or j == k:
                    continue
                res = 0
                for l in range(N):
                    for m in range(N):
                        if (l + m) % 3 == 0:
                            res += D[c[l][m] - 1][i]
                        elif (l + m) % 3 == 1:
                            res += D[c[l][m] - 1][j]
                        else:
                            res += D[c[l][m] - 1][k]
                ans = min(ans, res)
    print(ans)
