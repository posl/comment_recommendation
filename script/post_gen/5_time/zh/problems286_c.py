Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, A, B = map(int, input().split())
    S = input()
    A_count = 0
    B_count = 0
    for i in range(N//2):
        if S[i] != S[-i-1]:
            if S[i] == "a":
                A_count += 1
            else:
                B_count += 1
    if A_count == 0 and B_count == 0:
        print(0)
    else:
        print(A_count*A+B_count*B)

=======
Suggestion 2

def solve():
    N, A, B = map(int, input().split())
    S = input()
    S = list(S)
    ans = 0
    k = 0
    for i in range(N // 2):
        if S[i] != S[N - 1 - i]:
            k += 1
    if k == 0:
        print(ans)
        return
    if A < B:
        ans += A * k
        print(ans)
        return
    else:
        ans += B * k
    if k == 1:
        print(ans)
        return
    if k == 2:
        ans += A
        print(ans)
        return
    if k == 3:
        ans += A * 2
        print(ans)
        return
    if k == 4:
        ans += A * 2
        print(ans)
        return
    if k == 5:
        ans += A * 3
        print(ans)
        return
    if k == 6:
        ans += A * 3
        print(ans)
        return
    if k == 7:
        ans += A * 4
        print(ans)
        return
    if k == 8:
        ans += A * 4
        print(ans)
        return
    if k == 9:
        ans += A * 4
        print(ans)
        return
    if k == 10:
        ans += A * 5
        print(ans)
        return
    if k == 11:
        ans += A * 5
        print(ans)
        return
    if k == 12:
        ans += A * 6
        print(ans)
        return
    if k == 13:
        ans += A * 6
        print(ans)
        return
    if k == 14:
        ans += A * 6
        print(ans)
        return
    if k == 15:
        ans += A * 7
        print(ans)
        return
    if k == 16:
        ans += A * 7
        print(ans)
        return
    if k == 17:
        ans += A * 7
        print(ans)
        return
    if k == 18:
        ans += A * 7
        print(ans)
        return
    if

=======
Suggestion 3

def solve(n, a, b, s):
    # 定义dp[i][j]为前i个字符，变为回文，最少需要花费的钱数
    # 有两种情况：
    # 1. 第i个字符不需要替换，即s[i] == s[n-i-1]
    # 2. 第i个字符需要替换，即s[i] != s[n-i-1]
    # 对于第一种情况，dp[i][j] = dp[i-1][j]
    # 对于第二种情况，dp[i][j] = dp[i-1][j] + a
    # 此外，还需要考虑第i个字符需要替换，但是第n-i-1个字符不需要替换的情况
    # dp[i][j] = min(dp[i][j], dp[i-1][j-1] + a)
    # 初始条件：
    # dp[0][0] = 0
    # dp[0][1] = a
    # dp[1][0] = a
    # dp[1][1] = 0
    # dp[1][2] = a
    # dp[2][0] = a*2
    # dp[2][1] = a
    # dp[2][2] = 0
    # dp[2][3] = a
    # dp[3][0] = a*3
    # dp[3][1] = a*2
    # dp[3][2] = a
    # dp[3][3] = 0
    # dp[3][4] = a
    # dp[4][0] = a*4
    # dp[4][1] = a*3
    # dp[4][2] = a*2
    # dp[4][3] = a
    # dp[4][4] = 0
    # dp[4][5] = a
    # dp[5][0] = a*5
    # dp[5][1] = a*4
    # dp[5][2] = a*3

=======
Suggestion 4

def main():
    n,a,b = map(int,input().split())
    s = input()
    if n%2==0:
        if a<b:
            print(a*n)
        else:
            print(b*n)
    else:
        if a<b:
            print(a*(n-1)+b)
        else:
            print(b*(n-1)+a)

=======
Suggestion 5

def main():
    N, A, B = map(int, input().split())
    S = input()
    count = 0
    for i in range(N):
        if S[i] != S[N - 1 - i]:
            if S[i] == 'a':
                count += A
            else:
                count += B
    if count == 0:
        print(0)
    elif count == A:
        print(A)
    elif count == B:
        print(B)
    else:
        print(2 * min(A, B))

=======
Suggestion 6

def is_palindrome(s):
    return s == s[::-1]

=======
Suggestion 7

def main():
    n, a, b = map(int, input().split())
    s = input()
    cnt = 0
    for i in range(n):
        if s[i] != s[n-i-1]:
            if s[i] == 'a':
                cnt += a
            else:
                cnt += b
        elif s[i] == s[n-i-1] and s[i] == 'a':
            cnt += a
        elif s[i] == s[n-i-1] and s[i] == 'b':
            cnt += b
    print(cnt)

=======
Suggestion 8

def main():
    n, a, b = map(int, input().split())
    s = input()

    if a < b:
        print(sum([a if s[i] == s[n - i - 1] else b for i in range(n // 2)]))
    else:
        print(sum([b if s[i] == s[n - i - 1] else a for i in range(n // 2)]))

=======
Suggestion 9

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
Suggestion 10

def solve():
    n, a, b = map(int, input().split())
    s = input()
    s = list(s)
    ans = 0
    for i in range(n // 2):
        if s[i] == s[n - 1 - i]:
            continue
        elif s[i] == 'a':
            s[n - 1 - i] = 'a'
            ans += a
        elif s[n - 1 - i] == 'a':
            s[i] = 'a'
            ans += a
        else:
            print(-1)
            return
    if n % 2 == 1 and s[n // 2] != 'a':
        s[n // 2] = 'a'
        ans += a
    for i in range(n):
        if s[i] != 'a':
            ans += b
    print(ans)
solve()
