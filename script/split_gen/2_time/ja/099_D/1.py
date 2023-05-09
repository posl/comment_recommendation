def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    for i in range(C):
        for j in range(C):
            for k in range(C):
                D[j][k] = min(D[j][k], D[j][i] + D[i][k])
    ans = float("inf")
    for i in range(C):
        for j in range(C):
            if i == j:
                continue
            for k in range(C):
                if i == k or j == k:
                    continue
                tmp = 0
                for l in range(N):
                    for m in range(N):
                        if (l + m) % 3 == 0:
                            tmp += D[c[l][m] - 1][i]
                        elif (l + m) % 3 == 1:
                            tmp += D[c[l][m] - 1][j]
                        else:
                            tmp += D[c[l][m] - 1][k]
                ans = min(ans, tmp)
    print(ans)
