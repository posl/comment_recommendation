def solve():
    #import sys
    #input = sys.stdin.readline
    s = input().rstrip()
    n = len(s)
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1, n+1):
        if s[i-1] == '(':
            dp[i] = dp[i-1]
        elif s[i-1] == ')':
            for j in range(i-1, -1, -1):
                if s[j-1] == '(':
                    dp[i] = dp[j-1]
                    break
        else:
            dp[i] = dp[i-1] + 1
    if dp[n] == 1:
        print('Yes')
    else:
        print('No')
solve()
