def solve(N, Q, A, x):
    A.sort()
    for i in range(Q):
        print(N - bisect.bisect_left(A, x[i]))
