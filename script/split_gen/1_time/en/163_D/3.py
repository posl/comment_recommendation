def main():
    N,K = map(int,input().split())
    MOD = 10**9+7
    ans = 0
    for i in range(K,N+2):
        a = (i-1)*i//2
        b = (N+i-1)*N//2
        ans += b-a+1
        ans %= MOD
    print(ans)
