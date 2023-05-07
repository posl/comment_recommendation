def main():
    X, Y = map(int, input().split())
    mod = 10**9+7
    if (X+Y)%3:
        print(0)
        return
    N = (X+Y)//3
    if X < Y:
        X, Y = Y, X
    if X > 2*N or Y > 2*N:
        print(0)
        return
    if X == 2*N:
        print(1)
        return
    if X == 2*N-1:
        print(N-Y+1)
        return
    if Y == 2*N:
        print(N-X+1)
        return
    if Y == 2*N-1:
        print(N-X+1)
        return
    fac = [1]*(N+1)
    for i in range(1, N+1):
        fac[i] = fac[i-1]*i%mod
    inv = [1]*(N+1)
    inv[N] = pow(fac[N], mod-2, mod)
    for i in range(N, 0, -1):
        inv[i-1] = inv[i]*i%mod
    def comb(n, r):
        if n < r:
            return 0
        return fac[n]*inv[r]*inv[n-r]%mod
    ans = 0
    for i in range(X-2*N+1):
        ans += comb(2*N-i, X-2*N-i)*comb(i, Y-2*N+i)
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()