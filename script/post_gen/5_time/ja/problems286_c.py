Synthesizing 9/10 solutions

=======
Suggestion 1

def solve():
    N,A,B = map(int,input().split())
    S = input()
    dp = [[float('inf')]*(N+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        dp[i+1][0] = dp[i][0] + B
        dp[i+1][1] = min(dp[i][0],dp[i][1]) + A
        for j in range(2,i+2):
            if S[i-j+1] == S[i]:
                dp[i+1][j] = dp[i][j-2]
            else:
                dp[i+1][j] = min(dp[i][j-2],dp[i][j-1]) + A
    print(min(dp[N]))

=======
Suggestion 2

def resolve():
    N,A,B = map(int,input().split())
    S = input()
    #print(N,A,B,S)

    #dp[i][j]は、i文字目まで見たときに、j文字を変える場合の最小値
    dp = [[float('inf')]*(N+1) for i in range(N+1)]
    dp[0][0] = 0

    for i in range(N):
        for j in range(N+1):
            if S[i] == S[N-1-i]:
                dp[i+1][j] = min(dp[i+1][j],dp[i][j])
            else:
                dp[i+1][j] = min(dp[i+1][j],dp[i][j]+A)
                if j < N:
                    dp[i+1][j+1] = min(dp[i+1][j+1],dp[i][j]+B)

    ans = float('inf')
    for i in range(N+1):
        ans = min(ans,dp[N][i]+A*i)
    print(ans)

=======
Suggestion 3

def main():
    n, a, b = map(int, input().split())
    s = input()
    s = list(s)
    s.reverse()
    #print(s)
    #print(s[0])
    #print(s[n-1])
    #print(s[n-1] == s[0])
    #print(s[n-2] == s[1])
    #print(s[n-3] == s[2])
    #print(s[n-4] == s[3])
    #print(s[n-5] == s[4])
    #print(s[n-6] == s[5])
    #print(s[n-7] == s[6])
    #print(s[n-8] == s[7])
    #print(s[n-9] == s[8])
    #print(s[n-10] == s[9])
    #print(s[n-11] == s[10])
    #print(s[n-12] == s[11])
    #print(s[n-13] == s[12])
    #print(s[n-14] == s[13])
    #print(s[n-15] == s[14])
    #print(s[n-16] == s[15])
    #print(s[n-17] == s[16])
    #print(s[n-18] == s[17])
    #print(s[n-19] == s[18])
    #print(s[n-20] == s[19])
    #print(s[n-21] == s[20])
    #print(s[n-22] == s[21])
    #print(s[n-23] == s[22])
    #print(s[n-24] == s[23])
    #print(s[n-25] == s[24])
    #print(s[n-26] == s[25])
    #print(s[n-27] == s[26])
    #print(s[n-28] == s[27])
    #print(s[n-29] == s[28])
    #print(s[n-30] == s[29])
    #print(s[n-31] == s[30])
    #print(s[n-32] == s[31])
    #print(s[n-33] == s[32])
    #print(s[n-34] == s[33])
    #print(s[n-35

=======
Suggestion 4

def is_palindrome(S):
    for i in range(len(S)//2):
        if S[i] != S[-i-1]:
            return False
    return True

N,A,B = map(int,input().split())
S = input()

=======
Suggestion 5

def check(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True

=======
Suggestion 6

def solve():
    #n, a, b = map(int, input().split())
    #s = input()
    n, a, b = 5, 1, 2
    s = 'rrefa'
    print(n, a, b)
    print(s)

    #dp = [[0] * n for _ in range(n)]
    #for i in range(n):
    #    dp[i][i] = 0
    #for i in range(n - 1):
    #    dp[i][i + 1] = 0 if s[i] == s[i + 1] else 1

    #for i in range(3, n):
    #    for j in range(n - i):
    #        if s[j] == s[j + i]:
    #            dp[j][j + i] = dp[j + 1][j + i - 1]
    #        else:
    #            dp[j][j + i] = min(dp[j + 1][j + i] + 1, dp[j][j + i - 1] + 1)

    #print(dp[0][n - 1])
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0
    for i in range(n - 1):
        dp[i][i + 1] = 0 if s[i] == s[i + 1] else 1

    for i in range(3, n):
        for j in range(n - i):
            if s[j] == s[j + i]:
                dp[j][j + i] = dp[j + 1][j + i - 1]
            else:
                dp[j][j + i] = min(dp[j + 1][j + i] + 1, dp[j][j + i - 1] + 1)

    print(dp[0][n - 1])

=======
Suggestion 7

def solve(n,a,b,s):
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n):
        dp[i][i] = 0
    for i in range(n-1):
        dp[i][i+1] = 0
        if s[i] == s[i+1]:
            dp[i][i+1] = 0
        else:
            dp[i][i+1] = a
    for i in range(2,n):
        for j in range(n-i):
            if s[j] == s[j+i]:
                dp[j][j+i] = dp[j+1][j+i-1]
            else:
                dp[j][j+i] = min(dp[j+1][j+i]+a,dp[j][j+i-1]+a,b+dp[j+1][j+i-1])
    return dp[0][n-1]

=======
Suggestion 8

def main():
    N, A, B = map(int, input().split())
    S = input()
    S = list(S)
    S.reverse()
    S = ''.join(S)
    #print(N, A, B, S)
    #print(S[0])
    #print(S[1])
    #print(S[-1])
    #print(S[-2])

    #print(S)
    #print(S[0])
    #print(S[1])
    #print(S[-1])
    #print(S[-2])

    #print(S[0])
    #print(S[-1])
    #print(S[0] == S[-1])
    #print(S[1])
    #print(S[-2])
    #print(S[1] == S[-2])

    #print(S[0])
    #print(S[-1])
    #print(S[0] == S[-1])
    #print(S[1])
    #print(S[-2])
    #print(S[1] == S[-2])

    #print(S[0])
    #print(S[-1])
    #print(S[0] == S[-1])
    #print(S[1])
    #print(S[-2])
    #print(S[1] == S[-2])

    #print(S[0])
    #print(S[-1])
    #print(S[0] == S[-1])
    #print(S[1])
    #print(S[-2])
    #print(S[1] == S[-2])

    #print(S[0])
    #print(S[-1])
    #print(S[0] == S[-1])
    #print(S[1])
    #print(S[-2])
    #print(S[1] == S[-2])

    #print(S[0])
    #print(S[-1])
    #print(S[0] == S[-1])
    #print(S[1])
    #print(S[-2])
    #print(S[1] == S[-2])

    #print(S[0])
    #print(S[-1])
    #print(S[0] == S[-1])
    #print(S[1])
    #print(S[-2])
    #print(S[1] == S[-2])

    #print(S[0])
    #print(S[-1])
    #print(S[0] == S[-1])

=======
Suggestion 9

def main():
    n, a, b = map(int, input().split())
    s = input()
    min_cost = 0
    for i in range(n//2):
        if s[i] == s[-i-1]:
            continue
        elif s[i] == 'a' or s[-i-1] == 'a':
            min_cost += a
        else:
            print(-1)
            exit()
    if n%2 == 1 and s[n//2] != 'a':
        min_cost += a
    print(min_cost)
