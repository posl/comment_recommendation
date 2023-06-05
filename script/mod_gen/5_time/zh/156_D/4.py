def main():
    n,a,b = map(int,input().split())
    mod = 10**9+7
    if a+b>n:
        print(0)
        return
    ans = pow(2,n,mod)-1
    def cmb(n,r,mod):
        if r==0:return 1
        if r<0:return 0
        if (n-r)<r:r=n-r
        num = den = 1
        for i in range(r):
            num = num*(n-i)%mod
            den = den*(i+1)%mod
        return num*pow(den,mod-2,mod)%mod
    print((ans-cmb(n,a,mod)-cmb(n,b,mod))%mod)

if __name__ == '__main__':
    main()