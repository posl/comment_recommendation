def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # dp[i] = i 個の石があるときに、高橋君が最大何個取り除けるか
    dp = [0] * (N + 1)
    for i in range(N + 1):
        for j in range(K):
            if i - A[j] < 0:
                break
            if dp[i - A[j]] == 0:
                dp[i] = 1
                break
    if dp[N] == 1:
        print("Takahashi")
    else:
        print("Aoki")

if __name__ == '__main__':
    main()