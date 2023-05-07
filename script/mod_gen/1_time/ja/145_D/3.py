def main():
    X,Y = map(int, input().split())
    if (X+Y)%3 != 0:
        print(0)
        exit()
    n = (2*Y-X)//3
    m = (2*X-Y)//3
    if n < 0 or m < 0:
        print(0)
        exit()
    mod = 10**9+7
    fact = [1,1]
    for i in range(2,n+m+1):
        fact.append((fact[-1]*i)%mod)
    invfact = [1,1]
    for i in range(2,n+m+1):
        invfact.append((invfact[-1]*pow(i,mod-2,mod))%mod)
    print((fact[n+m]*invfact[n]*invfact[m])%mod)

if __name__ == '__main__':
    main()