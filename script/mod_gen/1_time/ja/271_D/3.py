def main():
    N, S = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    dp = [[0] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(S + 1):
            if dp[i][j] == 0:
                continue
            if j + A[i] <= S:
                dp[i + 1][j + A[i]] = 1
            if j + B[i] <= S:
                dp[i + 1][j + B[i]] = 2
    if dp[N][S] == 0:
        print("No")
        return
    ans = ""
    now = S
    for i in range(N, 0, -1):
        if dp[i][now] == 1:
            ans += "H"
            now -= A[i - 1]
        else:
            ans += "T"
            now -= B[i - 1]
    print("Yes")
    print(ans[::-1])

if __name__ == '__main__':
    main()