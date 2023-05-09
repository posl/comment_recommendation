def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = A[i] - (i + 1)
    B.sort()
    if N % 2 == 0:
        print(B[N // 2] + B[N // 2 - 1] + 1)
    else:
        print(B[N // 2] * 2 + 1)
