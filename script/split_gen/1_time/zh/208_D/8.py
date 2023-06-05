def main():
    n,m = map(int,input().split())
    d = [[float("inf")]*n for _ in range(n)]
    for i in range(n):
        d[i][i] = 0
    for i in range(m):
        a,b,c = map(int,input().split())
        d[a-1][b-1] = c
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k]+d[k][j])
    ans = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i == j or j == k or k == i:
                    continue
                ans += d[i][j]+d[j][k]
    print(ans)
