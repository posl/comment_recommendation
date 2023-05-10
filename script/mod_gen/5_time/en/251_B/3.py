def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = A[:N]
    dp = [[0 for _ in range(W+1)] for _ in range(4)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(3, -1, -1):
            for k in range(W+1):
                if dp[j][k] == 1 and k + A[i] <= W:
                    dp[j+1][k+A[i]] = 1
    ans = 0
    for j in range(4):
        for k in range(W+1):
            if dp[j][k] == 1:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()