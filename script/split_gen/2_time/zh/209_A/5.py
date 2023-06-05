def main():
    n,m = map(int, input().split())
    a = [[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        a[i][i] = 0
    for i in range(m):
        s,t,k = map(int, input().split())
        a[s-1][t-1] = k
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                a[i][j] = min(a[i][j], a[i][k]+a[k][j])
    
    ans = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if a[i][j] == a[i][k] + a[k][j]:
                    ans += a[i][j]
    print(ans)
