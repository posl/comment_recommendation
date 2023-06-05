def solve():
    N,K = map(int,input().split())
    MOD = 10**9+7
    ans = 0
    for i in range(K,N+2):
        min = i*(i-1)//2
        max = i*(N+N-i+1)//2
        ans += max - min + 1
        ans %= MOD
    print(ans)

if __name__ == '__main__':
    solve()