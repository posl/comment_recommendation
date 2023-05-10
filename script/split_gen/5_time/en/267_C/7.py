def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    maxSum = 0
    for i in range(1, N+1):
        maxSum += i * A[i-1]
    print(maxSum)
    return 0
