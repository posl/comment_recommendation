def isPermutation(A):
    N = len(A)
    for i in range(N):
        if not (A[i] >= 1 and A[i] <= N):
            return False
    return True
N = int(input())
A = list(map(int, input().split()))
