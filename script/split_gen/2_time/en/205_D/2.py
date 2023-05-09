def solve():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    A = [0] + A + [10**18]
    D = []
    for i in range(N+1):
        D.append(A[i+1] - A[i] - 1)
    D.sort(reverse=True)
    for k in K:
        if k <= D[0]:
            print(k)
        else:
            k -= D[0]
            print(A[N] + (k + N - 1) // N)
