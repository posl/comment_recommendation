def main():
    n, c = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(c)]
    c = [list(map(int, input().split())) for _ in range(n)]
    ans = 10**9
    for i in range(c):
        for j in range(c):
            for k in range(c):
                if i == j or j == k or k == i:
                    continue
                tmp = 0
                for l in range(n):
                    for m in range(n):
                        if (l+m)%3 == 0:
                            tmp += d[c[l][m]-1][i]
                        elif (l+m)%3 == 1:
                            tmp += d[c[l][m]-1][j]
                        else:
                            tmp += d[c[l][m]-1][k]
                ans = min(ans, tmp)
    print(ans)
