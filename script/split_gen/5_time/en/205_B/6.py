def is_permutation(A):
    N = len(A)
    for i in range(1, N+1):
        if i not in A:
            return False
    return True
N = int(input())
A = list(map(int, input().split()))
