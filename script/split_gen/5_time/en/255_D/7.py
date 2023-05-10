def solve():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    # A = [6, 11, 2, 5, 5]
    # X = [5, 20, 0]
    # N, Q = 5, 3
    # A = [1000000000, 314159265, 271828182, 141421356, 161803398, 0, 777777777, 255255255, 536870912, 998244353]
    # X = [555555555, 321654987, 1000000000, 789456123, 0]
    A.sort()
    # print(A)
    # print(X)
    s = sum(A)
    # print(s)
    for i in range(Q):
        x = X[i]
        # print(x)
        # print(A)
        # print(s)
        # print()
        j = 0
        while j < N and A[j] < x:
            j += 1
        # print(j)
        if j == N:
            print(s + (x - A[-1]))
        else:
            print(s - (N - j) * (x - A[j]))
