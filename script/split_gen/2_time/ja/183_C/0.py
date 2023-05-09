def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            for k in range(N):
                if i == k or j == k:
                    continue
                for l in range(N):
                    if i == l or j == l or k == l:
                        continue
                    for m in range(N):
                        if i == m or j == m or k == m or l == m:
                            continue
                        for n in range(N):
                            if i == n or j == n or k == n or l == n or m == n:
                                continue
                            for o in range(N):
                                if i == o or j == o or k == o or l == o or m == o or n == o:
                                    continue
                                for p in range(N):
                                    if i == p or j == p or k == p or l == p or m == p or n == p or o == p:
                                        continue
                                    if T[i][j] + T[j][k] + T[k][l] + T[l][m] + T[m][n] + T[n][o] + T[o][p] + T[p][i] == K:
                                        ans += 1
    print(ans)
