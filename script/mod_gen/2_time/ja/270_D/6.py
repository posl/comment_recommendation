def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    dp = [False] * (N+1)
    dp[0] = True
    for i in range(N+1):
        if dp[i] == True:
            for j in range(K):
                if i + A[j] <= N:
                    dp[i + A[j]] = True
    print(N - dp[::-1].index(True))

if __name__ == '__main__':
    main()