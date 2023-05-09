def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a - 1 for a in A]
    #print(A)
    dp = [0] * N
    for k in range(K):
        if dp[0] == 0:
            dp[0] = 1
            for i in range(N):
                dp[A[i]] += 1
        else:
            break
    #print(dp)
    if dp[0] == 0:
        print(A[K - 1] + 1)
    else:
        dp = [d / dp[0] for d in dp]
        K = K % dp[0]
        print(A[K - 1] + 1)

if __name__ == '__main__':
    main()