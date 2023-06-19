def   main ():
    n, k = map(int, input().split())
    t = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(1, n):
        t[i][0] += t[i-1][0]
    for i in range(1, n):
        t[0][i] += t[0][i-1]
    for i in range(1, n):
        for j in range(1, n):
            t[i][j] += t[i-1][j] + t[i][j-1] - t[i-1][j-1]
    for i in range(n):
        for j in range(n):
            for l in range(i, n):
                for m in range(j, n):
                    if i == 0 and j == 0:
                        tmp = t[l][m]
                    elif i == 0:
                        tmp = t[l][m] - t[l][j-1]
                    elif j == 0:
                        tmp = t[l][m] - t[i-1][m]
                    else:
                        tmp = t[l][m] - t[i-1][m] - t[l][j-1] + t[i-1][j-1]
                    if tmp == k:
                        ans += 1
    print(ans)
