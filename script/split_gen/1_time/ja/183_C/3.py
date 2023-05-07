def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for i in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            for k in range(N):
                if k == i or k == j:
                    continue
                for l in range(N):
                    if l == i or l == j or l == k:
                        continue
                    for m in range(N):
                        if m == i or m == j or m == k or m == l:
                            continue
                        for n in range(N):
                            if n == i or n == j or n == k or n == l or n == m:
                                continue
                            for o in range(N):
                                if o == i or o == j or o == k or o == l or o == m or o == n:
                                    continue
                                for p in range(N):
                                    if p == i or p == j or p == k or p == l or p == m or p == n or p == o:
                                        continue
                                    if T[i][j] + T[j][k] + T[k][l] + T[l][m] + T[m][n] + T[n][o] + T[o][p] == K:
                                        ans += 1
    print(ans)
