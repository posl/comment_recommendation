Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    T = input()
    min = 1000
    for i in range(len(S)-len(T)+1):
        count = 0
        for j in range(len(T)):
            if S[i+j] != T[j]:
                count += 1
        if count < min:
            min = count
    print(min)

=======
Suggestion 2

def main():
    s = input()
    t = input()
    ans = len(t)
    for i in range(len(s)-len(t)+1):
        cnt = 0
        for j in range(len(t)):
            if s[i+j] != t[j]:
                cnt += 1
        ans = min(ans,cnt)
    print(ans)

=======
Suggestion 3

def solve():
    s = input()
    t = input()
    ans = 1000
    for i in range(len(s)-len(t)+1):
        cnt = 0
        for j in range(len(t)):
            if s[i+j] != t[j]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 4

def main():
    S = input()
    T = input()
    min = len(T)
    for i in range(len(S)-len(T)+1):
        count = 0
        for j in range(len(T)):
            if S[i+j] != T[j]:
                count += 1
        if min > count:
            min = count
    print(min)

=======
Suggestion 5

def solve(s, t):
    # 动态规划
    # dp[i][j]表示s的前i个字符和t的前j个字符的最小编辑距离
    # dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+1)
    # dp[i][j] = dp[i-1][j-1] if s[i] == t[j] else dp[i-1][j-1]+1
    # dp[i][j] = dp[i-1][j-1] + 1 if s[i] != t[j] else dp[i-1][j-1]
    # dp[i][0] = i
    # dp[0][j] = j
    dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
    for i in range(1, len(s)+1):
        dp[i][0] = i
    for j in range(1, len(t)+1):
        dp[0][j] = j
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                # dp[i-1][j-1]+1 表示替换
                # dp[i-1][j]+1 表示删除
                # dp[i][j-1]+1 表示插入
                dp[i][j] = min(dp[i-1][j-1]+1, dp[i-1][j]+1, dp[i][j-1]+1)
    return dp[len(s)][len(t)]

=======
Suggestion 6

def solve():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    ans = m
    for i in range(n-m+1):
        cnt = 0
        for j in range(m):
            if s[i+j] != t[j]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 7

def solve():
    s = input()
    t = input()
    min = 1000
    for i in range(len(s)-len(t)+1):
        count = 0
        for j in range(len(t)):
            if s[i+j] != t[j]:
                count += 1
        if count < min:
            min = count
    print(min)

=======
Suggestion 8

def main():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    ans = m
    for i in range(n - m + 1):
        cnt = 0
        for j in range(m):
            if s[i + j] != t[j]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 9

def main():
    s = input()
    t = input()
    print(len(t) - max([s[i:].find(t) for i in range(len(s))]))

=======
Suggestion 10

def main():
    S = input()
    T = input()
    cnt = 0
    for i in range(len(S)-len(T)+1):
        tmp = 0
        for j in range(len(T)):
            if S[i+j] != T[j]:
                tmp += 1
        if cnt < tmp:
            cnt = tmp
    print(cnt)
main()
