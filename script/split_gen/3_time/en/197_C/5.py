def solve(A):
    N = len(A)
    if N == 1:
        return 0
    if N == 2:
        return A[0] ^ A[1]
    if N == 3:
        return min(A[0] ^ A[1] ^ A[2], A[0] ^ A[1] | A[2], A[0] | A[1] ^ A[2])
    return min(A[0] ^ A[1] ^ A[2] ^ A[3], A[0] ^ A[1] ^ A[2] | A[3], A[0] ^ A[1] | A[2] ^ A[3], A[0] | A[1] ^ A[2] ^ A[3])
N = int(input())
A = list(map(int, input().split()))
print(solve(A))
