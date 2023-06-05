Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    s = s[::-1]
    n = len(s)
    s += '0'
    ans = 0
    for i in range(n):
        if s[i] == '0':
            ans += 1
        else:
            if s[i+1] == '0':
                ans += 1
            else:
                ans += 2
    print(ans)

=======
Suggestion 2

def main():
    S = input()
    ans = 0
    i = len(S) - 1
    while i >= 0:
        if S[i] == '0':
            ans += 1
        else:
            break
        i -= 1
    print(ans)

=======
Suggestion 3

def main():
    #读入数据
    s = input()
    s = int(s)
    # print(s)

    #处理数据
    # print(type(s))
    # print(s)
    # print(s*100)
    # print(s*10)
    # print(s*10+1)
    # print(s*10+2)
    # print(s*10+3)
    # print(s*10+4)
    # print(s*10+5)
    # print(s*10+6)
    # print(s*10+7)
    # print(s*10+8)
    # print(s*10+9)
    # print(s*100+1)
    # print(s*100+2)
    # print(s*100+3)
    # print(s*100+4)
    # print(s*100+5)
    # print(s*100+6)
    # print(s*100+7)
    # print(s*100+8)
    # print(s*100+9)
    # print(s*1000+1)
    # print(s*1000+2)
    # print(s*1000+3)
    # print(s*1000+4)
    # print(s*1000+5)
    # print(s*1000+6)
    # print(s*1000+7)
    # print(s*1000+8)
    # print(s*1000+9)
    # print(s*10000+1)
    # print(s*10000+2)
    # print(s*10000+3)
    # print(s*10000+4)
    # print(s*10000+5)
    # print(s*10000+6)
    # print(s*10000+7)
    # print(s*10000+8)
    # print(s*10000+9)
    # print(s*100000+1)
    # print(s*100000+2)
    # print(s*100000+3)
    # print(s*100000+4)
    # print(s*100000+5)
    # print(s*100000+6)
    # print(s*100000+7)
    # print(s*100000+8)
    # print(s*100000+9)
    # print(s*1000000+1)
    # print

=======
Suggestion 4

def solve():
    s = input()
    n = len(s)
    dp = [float('inf') for _ in range(n+1)]
    dp[0] = 0
    for i in range(n):
        for j in range(i, n):
            if i == 0 and s[j] == '0':
                continue
            dp[j+1] = min(dp[j+1], dp[i] + 1)
            if j + 1 < n:
                dp[j+2] = min(dp[j+2], dp[i] + 1)
            if j + 2 < n:
                dp[j+3] = min(dp[j+3], dp[i] + 2)
    print(dp[n])

=======
Suggestion 5

def main():
    s = input()
    s = s[::-1]
    ans = 0
    for i in range(len(s)):
        if s[i] == '0':
            ans += 1
        else:
            break
    print(ans)

=======
Suggestion 6

def get_input():
    return input()

=======
Suggestion 7

def solve():
    S = int(input())
    print(S)

=======
Suggestion 8

def main():
    s = input()
    s_len = len(s)
    #print(s_len)
    #print(s[0])
    #print(s[1])
    #print(s[2])
    #print(s[3])
    #print(s[4])
    #print(s[5])
    #print(s[6])
    #print(s[7])
    #print(s[8])
    #print(s[9])
    #print(s[10])
    #print(s[11])
    #print(s[12])
    #print(s[13])
    #print(s[14])
    #print(s[15])
    #print(s[16])
    #print(s[17])
    #print(s[18])
    #print(s[19])
    #print(s[20])
    #print(s[21])
    #print(s[22])
    #print(s[23])
    #print(s[24])
    #print(s[25])
    #print(s[26])
    #print(s[27])
    #print(s[28])
    #print(s[29])
    #print(s[30])
    #print(s[31])
    #print(s[32])
    #print(s[33])
    #print(s[34])
    #print(s[35])
    #print(s[36])
    #print(s[37])
    #print(s[38])
    #print(s[39])
    #print(s[40])
    #print(s[41])
    #print(s[42])
    #print(s[43])
    #print(s[44])
    #print(s[45])
    #print(s[46])
    #print(s[47])
    #print(s[48])
    #print(s[49])
    #print(s[50])
    #print(s[51])
    #print(s[52])
    #print(s[53])
    #print(s[54])
    #print(s[55])
    #print(s[56])
    #print(s[57])
    #print(s[58])
    #print(s[59])
    #print(s[60])
    #print(s[61])
    #print(s[62])
    #print(s[63])
    #print(s[64])
    #print(s[65])
    #print(s[66])
    #print(s[67])
    #print(s

=======
Suggestion 9

def func(s):
    result = 0
    for i in range(len(s)):
        if s[i] == '0':
            result += 1
    return result + 1

=======
Suggestion 10

def main():
    S = input()
    N = len(S)
    # dp[i][j] := S[i] まで決めて, j を作るのに必要な操作の最小値
    dp = [[float('inf')] * 21 for _ in range(N + 1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(21):
            if dp[i][j] == float('inf'):
                continue
            if S[i] == '0':
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            else:
                dp[i + 1][(j + int(S[i])) % 21] = min(dp[i + 1][(j + int(S[i])) % 21], dp[i][j] + 1)
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
    print(dp[N][5])
