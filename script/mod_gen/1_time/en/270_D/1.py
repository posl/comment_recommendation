def main():
    N, K = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    dp = [0 for i in range(N+1)]
    for i in range(1, N+1):
        for j in range(K):
            if i - A[j] >= 0:
                if dp[i - A[j]] == 0:
                    dp[i] = 1
    if dp[N] == 1:
        print("Takahashi")
    else:
        print("Aoki")
main()

if __name__ == '__main__':
    main()