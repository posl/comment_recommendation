def   main ():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    x = [[0] * N for _ in range(N)]
    y = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(A[i]):
            x[i][j], y[i][j] = map(int, input().split())
            x[i][j] -= 1
    ans = 0
    for i in range(2 ** N):
        ok = True
        for j in range(N):
            if (i >> j) & 1:
                for k in range(A[j]):
                    if y[j][k] == 1:
                        if not ((i >> x[j][k]) & 1):
                            ok = False
                    else:
                        if (i >> x[j][k]) & 1:
                            ok = False
        if ok:
            ans = max(ans, bin(i).count("1"))
    print(ans)

if __name__ == '__main__':
    ()