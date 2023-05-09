def solve(N, M, A):
    if N == M:
        return sum([i * A[i] for i in range(1, N + 1)])
    elif N > M:
        return solve(M, M, A)
    else:
        A.sort()
        A = A[::-1]
        # print(A)
        B = [0] * (N + 1)
        for i in range(1, N + 1):
            B[i] = B[i - 1] + A[i - 1]
        # print(B)
        ans = 0
        for i in range(1, N + 1):
            ans = max(ans, B[i] + (M - i) * A[i - 1])
        return ans

if __name__ == '__main__':
    solve()