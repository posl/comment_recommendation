def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod
 
mod = 10**9+7 #出力の制限
N = 10**6  # N は必要分だけ用意する
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル
 
for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )
N,K = map(int,input().split())
for i in range(K):
    if i == 0:
        print(cmb(N-K+1,K,mod))
    else:
        print((cmb(N-K+1,K-i,mod)*cmb(K+i-1,i,mod))%mod)

if __name__ == '__main__':
    cmb()