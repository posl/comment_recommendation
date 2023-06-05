def solve():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [0 for i in range(N)]
    for i in range(N):
        if i % 2 == 0:
            B[0] += A[i]
        else:
            B[0] -= A[i]
    for i in range(1, N):
        B[i] = 2 * A[i - 1] - B[i - 1]
    print(' '.join([str(i) for i in B]))
