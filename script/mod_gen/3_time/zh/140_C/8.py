def max_sum(A, B):
    A[0] = B[0]
    for i in range(1, len(A)):
        A[i] = max(B[i-1], B[i])
    return sum(A)
N = int(input())
B = list(map(int, input().split()))
A = [0] * N
print(max_sum(A, B))
