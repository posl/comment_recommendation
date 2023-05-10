def main():
    n, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    a = [[0 for _ in range(n+1)]] + [[0] + a[i] for i in range(n)]
    for i in range(n+1):
        for j in range(n):
            a[i][j+1] += a[i][j]
    for j in range(n+1):
        for i in range(n):
            a[i+1][j] += a[i][j]
    def f(x):
        for i in range(n-k+1):
            for j in range(n-k+1):
                if a[i+k][j+k] + a[i][j] - a[i+k][j] - a[i][j+k] >= x:
                    return True
        return False
    l, r = -1, 10**9+1
    while r-l > 1:
        m = (l+r)//2
        if f(m):
            l = m
        else:
            r = m
    print(l)
