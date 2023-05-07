def main():
    N, K = map(int, input().split())
    MOD = 10**9+7
    ans = 0
    for i in range(K, N+2):
        mn = (i-1)*i//2
        mx = i*(2*N-i+1)//2
        ans += mx-mn+1
        ans %= MOD
    print(ans)
