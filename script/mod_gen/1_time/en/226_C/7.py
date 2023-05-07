def main():
    N = int(input())
    dp = [0]*(N+1)
    for i in range(N):
        T, K, *A = map(int, input().split())
        dp[i+1] = T + min(dp[j] for j in A)
    print(dp[-1])

if __name__ == '__main__':
    main()