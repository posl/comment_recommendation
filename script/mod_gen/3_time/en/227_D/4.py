def main():
    N, K = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    A.sort()
    if K == N:
        print(1)
        return
    if K == 1:
        print(A[-1])
        return
    if K == 2:
        print(A[-1] + A[-2])
        return
    # K >= 3
    # A[0] - 1, A[1] - 2, A[2] - 3, ... A[N-K] - (N-K)
    # A[N-K] - (N-K) + A[N-K+1] - (N-K+1) + ... + A[N-1] - (N-1)
    # (A[N-K] + A[N-K+1] + ... + A[N-1]) - (N-K) - (N-K+1) - ... - (N-1)
    # A[N-K] + A[N-K+1] + ... + A[N-1] - (N-K)(N-K+1)/2 - (N-1)(N-2)/2
    # A[N-K] + A[N-K+1] + ... + A[N-1] - (N-K)(N-K+1)/2 - (N-1)(N-2)/2
    # A[N-K] + A[N-K+1] + ... + A[N-1] - (N-K)(N-K+1)/2 - (N-1)(N-2)/2
    # A[N-K] + A[N-K+1] + ... + A[N-1] - (N-K)(N-K+1)/2 - (N-1)(N-2)/2
    # A[N-K] + A[N-K+1] + ... + A[N-1] - (N-K)(N-K+1)/2 - (N-1)(N-2)/2
    # A[N-K] + A[N-K+1] + ... + A[N-1] - (N-K)(N-K+1)/2 - (N-1)(N-2)/2
    # A[N-K] + A[N-K+1] + ... + A[N-1] - (N-K

if __name__ == '__main__':
    main()