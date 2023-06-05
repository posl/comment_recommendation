def main():
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    dp = [0 for _ in range(n)]
    dp[0] = 0
    dp[1] = 0
    dp[2] = 0
    for i in range(3, n):
        dp[i] = dp[i-1]
        for j in range(i-1):
            for k in range(j+1, i):
                if A[j] < A[k] < A[i]:
                    dp[i] += 1
    print(dp[n-1])
