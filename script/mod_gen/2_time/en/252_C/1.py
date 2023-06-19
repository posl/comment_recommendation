def main():
    N = int(input())
    S = [input() for i in range(N)]
    ans = 40
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    for m in range(10):
                        cnt = 0
                        for n in range(N):
                            if n == 0 and S[n][i] != '0':
                                cnt += 1
                            elif n == 1 and S[n][j] != '1':
                                cnt += 1
                            elif n == 2 and S[n][k] != '2':
                                cnt += 1
                            elif n == 3 and S[n][l] != '3':
                                cnt += 1
                            elif n == 4 and S[n][m] != '4':
                                cnt += 1
                        ans = min(ans, cnt)
    print(ans)
main()
