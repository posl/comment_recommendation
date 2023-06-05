def main():
    n = int(input())
    a = [list(map(int, input())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            p = a[i][j]
            for k in range(n):
                for l in range(n):
                    q = a[k][l]
                    b = [[0] * n for _ in range(n)]
                    b[i][j] = 1
                    b[k][l] = 1
                    for m in range(n):
                        for o in range(n):
                            if b[m][o] == 1:
                                continue
                            if (m == 0 or b[m - 1][o]) and (m == n - 1 or b[m + 1][o]) and (o == 0 or b[m][o - 1]) and (o == n - 1 or b[m][o + 1]):
                                b[m][o] = 1
                    t = 0
                    for m in range(n):
                        for o in range(n):
                            if b[m][o] == 1:
                                t += a[m][o]
                    ans = max(ans, t - p - q)
    print(ans)
