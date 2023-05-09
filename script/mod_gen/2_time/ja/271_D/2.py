def main():
    N, S = map(int, input().split())
    a = [0] * N
    b = [0] * N
    for i in range(N):
        a[i], b[i] = map(int, input().split())
    dp = [[False for i in range(S+1)] for j in range(N+1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S+1):
            if dp[i][j]:
                if j + a[i] <= S:
                    dp[i+1][j+a[i]] = True
                if j + b[i] <= S:
                    dp[i+1][j+b[i]] = True
    if dp[N][S]:
        print("Yes")
        ans = ""
        while N > 0:
            if dp[N-1][S-a[N-1]]:
                ans += "H"
                S -= a[N-1]
            else:
                ans += "T"
                S -= b[N-1]
            N -= 1
        print(ans[::-1])
    else:
        print("No")

if __name__ == '__main__':
    main()