def solve(N, K, H):
    H.sort()
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans, H[i+K-1]-H[i])
    return ans

if __name__ == '__main__':
    solve()