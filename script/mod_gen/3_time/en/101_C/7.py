def solve(N, K, A):
    # N: length of the sequence
    # K: number of consecutive elements to be replaced
    # A: the sequence
    # return: the minimum number of operations required
    if N == K:
        return 1
    if K % 2 == 0:
        for i in range(N):
            if A[i] != i + 1:
                return (N - 1) // (K // 2) + 1
        return 1
    else:
        for i in range(N):
            if A[i] != N - i:
                return (N - 1) // (K // 2) + 1
        return 1

if __name__ == '__main__':
    solve()