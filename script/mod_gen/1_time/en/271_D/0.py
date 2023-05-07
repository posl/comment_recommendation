def main():
    N, S = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    if sum(a) < S:
        print("No")
        return
    if sum(b) > S:
        print("No")
        return
    dp = [[False for j in range(S+1)] for i in range(N+1)]
    dp[0][0] = True
    for i in range(1, N+1):
        for j in range(S+1):
            if j - a[i-1] >= 0:
                dp[i][j] = dp[i-1][j-a[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    if dp[N][S]:
        print("Yes")
        ans = []
        j = S
        for i in range(N, 0, -1):
            if j - a[i-1] >= 0:
                if dp[i-1][j-a[i-1]]:
                    ans.append("H")
                    j = j - a[i-1]
                else:
                    ans.append("T")
            else:
                ans.append("T")
        print("".join(ans[::-1]))
    else:
        print("No")

if __name__ == '__main__':
    main()