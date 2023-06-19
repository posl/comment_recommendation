def main():
    n,k = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(n)]
    def check(x):
        s = [[0]*(n+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(n):
                s[i+1][j+1] = s[i+1][j]+s[i][j+1]-s[i][j]+(1 if a[i][j]>=x else 0)
        for i in range(n-k+1):
            for j in range(n-k+1):
                if s[i+k][j+k]+s[i][j]-s[i+k][j]-s[i][j+k]>=(k*k+1)//2:
                    return True
        return False
    lb,ub = 0,10**9+1
    while ub-lb>1:
        mid = (lb+ub)//2
        if check(mid):
            lb = mid
        else:
            ub = mid
    print(lb)

if __name__ == '__main__':
    main()