Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,a,b = map(int,input().split())
    s = input()
    s1 = s[::-1]
    if s == s1:
        print(a*n+b*(n-1))
    else:
        s2 = s1[::-1]
        s3 = s2[0:n//2]
        if s3 == s:
            print(a*n+b*(n-1))
        else:
            s4 = s3[::-1]
            s5 = s2[n//2+1:n]
            if s4 == s5:
                print(a*n+b*(n-1))
            else:
                print(a*n+b*n)

=======
Suggestion 2

def solve():
    n, a, b = map(int, input().split())
    s = input()
    if a < b:
        print(a*n+b)
    else:
        print(b*n)

=======
Suggestion 3

def is_palindrome(s):
    return s == s[::-1]

=======
Suggestion 4

def main():
    N,A,B = map(int,input().split())
    S = input()
    #print(N,A,B,S)
    #print(type(N),type(A),type(B),type(S))
    #print(len(S))
    #print(S[0])
    #print(S[1])
    #print(S[2])
    #print(S[3])
    #print(S[4])
    #print(S[5])
    #print(S[6])
    #print(S[7])
    #print(S[8])
    #print(S[9])
    #print(S[10])
    #print(S[11])
    #print(S[12])
    #print(S[13])
    #print(S[14])
    #print(S[15])
    #print(S[16])
    #print(S[17])
    #print(S[18])
    #print(S[19])
    #print(S[20])
    #print(S[21])
    #print(S[22])
    #print(S[23])
    #print(S[24])
    #print(S[25])
    #print(S[26])
    #print(S[27])
    #print(S[28])
    #print(S[29])
    #print(S[30])
    #print(S[31])
    #print(S[32])
    #print(S[33])
    #print(S[34])
    #print(S[35])
    #print(S[36])
    #print(S[37])
    #print(S[38])
    #print(S[39])
    #print(S[40])
    #print(S[41])
    #print(S[42])
    #print(S[43])
    #print(S[44])
    #print(S[45])
    #print(S[46])
    #print(S[47])
    #print(S[48])
    #print(S[49])
    #print(S[50])
    #print(S[51])
    #print(S[52])
    #print(S[53])
    #print(S[54])
    #print(S[55])
    #print(S[56])
    #print(S[57])
    #print(S[58])
    #print(S[59])
    #print(S[60])
    #print(S[61])
    #print(S[62])
    #print(S[63])
    #print(S[

=======
Suggestion 5

def main():
    N, A, B = map(int, input().split())
    S = input()

    cnt = 0
    cnt_b = 0
    for i in range(N):
        if S[i] != S[N - i - 1]:
            if S[i] == 'a' or S[N - i - 1] == 'a':
                cnt_b += 1
            else:
                print(-1)
                return
        elif S[i] == 'a':
            cnt += 1

    if cnt_b == 0:
        print(0)
        return

    if cnt == N:
        print(A * N + B * (N - 1))
        return

    if S[N // 2] == 'a':
        print(A * N + B * cnt_b)
    else:
        print(A * N + B * (cnt_b - 1))

=======
Suggestion 6

def is_palindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False

=======
Suggestion 7

def solve():
    n, a, b = map(int, input().split())
    s = input()
    if n % 2 == 0:
        print(min(a * n, b * (n // 2)))
    else:
        print(min(a * n, b * (n // 2) + a))

=======
Suggestion 8

def func():
    pass

=======
Suggestion 9

def solve(n, a, b, s):
    # dp[i][j] = min cost to make s[i:j+1] a palindrome
    # dp[i][j] = min(dp[i+1][j] + a, dp[i][j-1] + a, dp[i+1][j-1] + b if s[i] != s[j])
    dp = [[0] * n for _ in range(n)]
    for j in range(n):
        for i in range(n - j):
            if i == j + i:
                continue
            if s[i] == s[j + i]:
                dp[i][j + i] = dp[i + 1][j + i - 1]
            else:
                dp[i][j + i] = min(dp[i + 1][j + i] + a, dp[i][j + i - 1] + a, dp[i + 1][j + i - 1] + b)
    return dp[0][n - 1]

n, a, b = map(int, input().split())
s = input()
print(solve(n, a, b, s))
