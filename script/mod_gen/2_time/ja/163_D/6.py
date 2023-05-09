def solve(N, K):
    mod = 10**9 + 7
    ans = 0
    for i in range(K, N+2):
        ans += (N+1)*N//2 - (N-i+1)*i//2 + 1
        ans %= mod
    return ans

if __name__ == '__main__':
    solve()