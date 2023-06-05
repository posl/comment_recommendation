def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    #d[i][j] = inf (iからjへ直接行く辺がない場合)
    #d[i][i] = 0
    n = len(d)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])
    return d
n,m = map(int,input().split())
d = [[float("inf") for i in range(n)] for j in range(n)]
for i in range(m):
    a,b,c = map(int,input().split())
    d[a-1][b-1] = c
d = warshall_floyd(d)
ans = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if d[i][j] == d[i][k] + d[k][j]:
                ans += d[i][j]
print(ans)

if __name__ == '__main__':
    warshall_floyd()