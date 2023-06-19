def solve(N, A):
    A = sorted(A)
    ans = 0
    for i in range(N):
        ans += A[i] - A[0]
    return ans

if __name__ == '__main__':
    solve()