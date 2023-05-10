def main():
    n,k = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(n)]
    b = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            b[i+1][j+1] = a[i][j]
    for i in range(n):
        for j in range(n):
            b[i+1][j+1] += b[i+1][j]
    for j in range(n):
        for i in range(n):
            b[i+1][j+1] += b[i][j+1]
    ans = 10**9
    for i in range(n-k+1):
        for j in range(n-k+1):
            x = b[i+k][j+k]-b[i][j+k]-b[i+k][j]+b[i][j]
            ans = min(ans,x)
    print(ans)
