def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [x-1 for x in A]
    dp = [0]*N
    dp[0] = 1
    for i in range(K):
        dp = [sum(dp) for x in dp]
        dp = [x%1000000007 for x in dp]
        dp[A[i]] -= 1
    print(dp[0])
main()

if __name__ == '__main__':
    main()