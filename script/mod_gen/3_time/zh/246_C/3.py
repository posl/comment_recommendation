def solve(N, K, X, A):
    ans = 0
    for i in range(N):
        if A[i] > X:
            ans += A[i] - X
    return ans

if __name__ == '__main__':
    solve()