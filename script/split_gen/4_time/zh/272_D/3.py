def main():
    n,m = map(int,input().split())
    from math import sqrt
    sqm = round(sqrt(m))
    if sqm**2 == m:
        sqm += 1
    ans = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            ans[i][j] = 10**9
            for k in range(i+1):
                for l in range(j+1):
                    if (i-k)**2+(j-l)**2 == m:
                        ans[i][j] = min(ans[i][j],ans[k][l]+1)
                    if (i-l)**2+(j-k)**2 == m:
                        ans[i][j] = min(ans[i][j],ans[k][l]+1)
    for i in range(n):
        for j in range(n):
            if ans[i][j] == 10**9:
                ans[i][j] = -1
    for i in range(n):
        print(*ans[i])
