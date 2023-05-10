def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    dp = [0 for _ in range(N+1)]
    for i in range(1,N+1):
        for j in range(K):
            if i - A[j] >= 0 and dp[i-A[j]] == 0:
                dp[i] = 1
    if dp[N] == 1:
        print("First")
    else:
        print("Second")

if __name__ == '__main__':
    main()