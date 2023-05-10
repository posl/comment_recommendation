def solve():
    N = int(input())
    T = [0] * N
    X = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], X[i], A[i] = map(int, input().split())
    max_sum = 0
    for i in range(N):
        if i == 0:
            max_sum = A[i]
            continue
        if T[i] - T[i-1] >= abs(X[i] - X[i-1]):
            max_sum += A[i]
    print(max_sum)
