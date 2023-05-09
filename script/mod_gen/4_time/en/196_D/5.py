def main():
    H, W, A, B = map(int, input().split())
    MOD = 10**9 + 7
    def cmb(n, r):
        if r < 0 or r > n:
            return 0
        r = min(r, n - r)
        return g1[n] * g2[r] * g2[n-r] % MOD
    N = H + W
    g1 = [1, 1] # 元テーブル
    g2 = [1, 1] #逆元テーブル
    inverse = [0, 1] #逆元テーブル計算用テーブル
    for i in range( 2, N + 1 ):
        g1.append( ( g1[-1] * i ) % MOD )
        inverse.append( ( -inverse[MOD % i] * (MOD//i) ) % MOD )
        g2.append( (g2[-1] * inverse[-1]) % MOD )
    ans = 0
    for i in range(B, W):
        ans += cmb(H-A-1+i, i) * cmb(A-1+W-i-1, A-1)
        ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()