def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [0] * (N+1)
    for i in range(N):
        if dp[i] == 0:
            for a in A:
                if i+a <= N:
                    dp[i+a] = 1
    if dp[N] == 1:
        print("Second")
    else:
        print("First")

if __name__ == '__main__':
    main()