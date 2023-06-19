def main():
    n, a, b = map(int, input().split())
    mod = 10**9+7
    ans = pow(2, n, mod) - 1
    nca = 1
    ncb = 1
    for i in range(a):
        nca *= n-i
        nca %= mod
        nca *= pow(i+1, mod-2, mod)
        nca %= mod
    for i in range(b):
        ncb *= n-i
        ncb %= mod
        ncb *= pow(i+1, mod-2, mod)
        ncb %= mod
    ans -= nca
    ans -= ncb
    print(ans%mod)

if __name__ == '__main__':
    main()