def main():
    MOD = 10**9+7
    X, Y = map(int, input().split())
    if (X+Y)%3 != 0:
        print(0)
        return
    N = (X+Y)//3
    if X>N or Y>N:
        print(0)
        return
    def comb(n, r):
        if r<0 or r>n:
            return 0
        r = min(r, n-r)
        return fac[n]*facinv[r]*facinv[n-r]%MOD
    fac = [1, 1]
    facinv = [1, 1]
    inv = [0, 1]
    for i in range(2, N+1):
        fac.append(fac[-1]*i%MOD)
        inv.append((-inv[MOD%i]*(MOD//i))%MOD)
        facinv.append(facinv[-1]*inv[-1]%MOD)
    print(comb(N, X))
