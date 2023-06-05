def main():
    n,k = map(int, input().split())
    mod = 10**9+7
    a = [0]*(n+1)
    for i in range(1,n+1):
        a[i] = (a[i-1]+pow(i,k,mod))%mod
    b = [0]*(n+1)
    for i in range(1,n+1):
        b[i] = (b[i-1]+pow(i,k-1,mod))%mod
    for i in range(1,k+1):
        ans = a[n]
        ans -= b[i]
        ans %= mod
        ans *= pow(i,mod-2,mod)
        ans %= mod
        print(ans)

if __name__ == '__main__':
    main()