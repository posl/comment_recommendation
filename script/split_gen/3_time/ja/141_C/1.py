def solve():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    B = [0] * N
    for i in range(Q):
        B[A[i]-1] += 1
    for i in range(N):
        if K - (Q - B[i]) > 0:
            print("Yes")
        else:
            print("No")
