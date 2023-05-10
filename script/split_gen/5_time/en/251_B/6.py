def solve():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = A[:N]
    #print(A)
    dp = [0] * (W+1)
    dp[0] = 1
    for i in range(N):
        for j in range(W, -1, -1):
            if dp[j] == 1 and j + A[i] <= W:
                dp[j+A[i]] = 1
    print(sum(dp))
