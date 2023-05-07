def main():
    n,k = map(int, input().split())
    mod = 10**9+7
    ans = 0
    for i in range(k,n+2):
        tmp = (i*(i-1)//2)%mod
        tmp2 = (n*(n+1)//2)%mod
        tmp3 = ((n-i+1)*(n-i+2)//2)%mod
        ans += tmp*tmp2 - tmp*tmp3
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()