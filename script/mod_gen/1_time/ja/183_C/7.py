def main():
    # 入力
    N, K = map(int, input().split())
    T = []
    for i in range(N):
        T.append(list(map(int, input().split())))
    # 組み合わせ全探索
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                for l in range(N):
                    for m in range(N):
                        for n in range(N):
                            for o in range(N):
                                for p in range(N):
                                    if i == j or i == k or i == l or i == m or i == n or i == o or i == p:
                                        continue
                                    if j == k or j == l or j == m or j == n or j == o or j == p:
                                        continue
                                    if k == l or k == m or k == n or k == o or k == p:
                                        continue
                                    if l == m or l == n or l == o or l == p:
                                        continue
                                    if m == n or m == o or m == p:
                                        continue
                                    if n == o or n == p:
                                        continue
                                    if o == p:
                                        continue
                                    if T[i][j] + T[j][k] + T[k][l] + T[l][m] + T[m][n] + T[n][o] + T[o][p] == K:
                                        ans += 1
    # 出力
    print(ans)

if __name__ == '__main__':
    main()