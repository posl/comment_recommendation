def main():
    n = int(input())
    p = [int(i) for i in input().split()]
    dp = [0 for i in range(n)]
    for i in p:
        dp[i-1] = dp[i-2]+1
    print(dp[-1])
