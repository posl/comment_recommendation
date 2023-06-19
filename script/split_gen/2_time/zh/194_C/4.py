def solve(N, A):
    sum = 0
    for i in range(1, N):
        for j in range(0, i):
            sum += (A[i] - A[j]) ** 2
    return sum
