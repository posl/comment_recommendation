def main():
    n,k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    b = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            b[i+1][j+1] = a[i][j]
    for i in range(n):
        for j in range(n):
            b[i+1][j+1] += b[i+1][j]
    for i in range(n):
        for j in range(n):
            b[i+1][j+1] += b[i][j+1]
    def check(x):
        for i in range(n-k+1):
            for j in range(n-k+1):
                if (b[i+k][j+k]-b[i+k][j]-b[i][j+k]+b[i][j]) >= x:
                    return True
        return False
    def solve():
        lb = -1
        ub = 10**9+1
        while ub-lb > 1:
            mid = (ub+lb)//2
            if check(mid):
                lb = mid
            else:
                ub = mid
        return lb
    ans = solve()
    print(ans)

if __name__ == '__main__':
    main()