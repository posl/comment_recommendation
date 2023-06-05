def get_min_non_negative_integer(N, A):
    A.sort()
    if A[0] != 0:
        return 0
    for i in range(N-1):
        if A[i+1] - A[i] > 1:
            return A[i] + 1
    return A[N-1] + 1
N = int(input())
A = list(map(int, input().split()))
print(get_min_non_negative_integer(N, A))
