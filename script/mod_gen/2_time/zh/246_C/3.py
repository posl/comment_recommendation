def solve(N, K, X, A):
    ans = 0
    for i in range(N):
        ans += max(A[i]-X, 0)
    return ans

if __name__ == '__main__':
    solve()