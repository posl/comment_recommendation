def solve():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    # print(A)
    # print(P, Q, R)
    # print(N)
    for i in range(N - 2):
        if A[i] <= P and A[i + 1] <= Q and A[i + 2] <= R:
            return 'Yes'
    return 'No'
print(solve())
