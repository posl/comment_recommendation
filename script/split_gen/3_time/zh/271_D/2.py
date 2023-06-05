def main():
    n,s = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        a_i,b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    #print(a,b)
    #dp[i][j]表示前i张牌中，和为j的情况下，第i张牌的正反面状态
    dp = [[0 for i in range(s+1)] for j in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(s+1):
            if dp[i][j]:
                dp[i+1][j] = 1
                if j+a[i] <= s:
                    dp[i+1][j+a[i]] = 2
                if j+b[i] <= s:
                    dp[i+1][j+b[i]] = 3
    #print(dp)
    if dp[n][s] == 0:
        print("No")
    else:
        print("Yes")
        ans = ""
        for i in range(n,0,-1):
            if dp[i][s] == 2:
                ans += "H"
                s -= a[i-1]
            else:
                ans += "T"
                s -= b[i-1]
        print(ans[::-1])
