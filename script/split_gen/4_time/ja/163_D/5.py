def main():
    N,K = map(int,input().split())
    mod = 10**9+7
    ans = 0
    for i in range(K,N+2):
        ans += (i*(2*N-i+1)//2) - (i*(i-1)//2) + 1
        ans = ans % mod
    print(ans)
