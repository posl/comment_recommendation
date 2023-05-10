def solve(N, K, P):
    ans = 0
    for i in range(N-K+1):
        ans = max(ans, sum(P[i:i+K])/K)
    return ans

if __name__ == '__main__':
    solve()