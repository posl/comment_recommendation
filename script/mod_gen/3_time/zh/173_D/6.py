def solve(N, A):
    sum = 0
    for i in range(N-1):
        sum += A[i]
    max = 0
    for i in range(N):
        if A[i] > max:
            max = A[i]
    return sum - max
N = int(input())
A = list(map(int, input().split()))
print(solve(N, A))
