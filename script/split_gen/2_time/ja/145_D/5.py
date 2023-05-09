def main():
    X, Y = map(int, input().split())
    MOD = 10**9+7
    if (X+Y)%3 != 0:
        print(0)
        return
    N = (X+Y)//3
    if X>N or Y>N:
        print(0)
        return
    def cmb(n, r, mod):
        if n<r:
            return 0
        r = min(r, n-r)
        return g1[n] * g2[r] * g2[n-r] % mod
    N = 2*10**6
    g1 = [1, 1] # 元テーブル
    g2 = [1, 1] #逆元テーブル
    inverse = [0, 1] #逆元テーブル計算用テーブル
    for i in range( 2, N + 1 ):
        g1.append( ( g1[-1] * i ) % MOD )
        inverse.append( ( -inverse[MOD % i] * (MOD//i) ) % MOD )
        g2.append( (g2[-1] * inverse[-1]) % MOD )
    print(cmb(N, N-X, MOD))
