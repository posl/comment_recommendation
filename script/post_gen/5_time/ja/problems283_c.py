Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    S = S[::-1]
    S = int(S)
    count = 0
    while True:
        if S == 0:
            break
        if S % 10 == 0:
            S = S // 10
            count += 1
        else:
            count += S % 10
            S = S - S % 10
    print(count)

=======
Suggestion 2

def main():
    S = int(input())
    # S = 10888869450418352160768000001
    # S = 1355506027
    # S = 40004
    # S = 1
    # S = 2
    # S = 3
    # S = 4
    # S = 5
    # S = 6
    # S = 7
    # S = 8
    # S = 9
    # S = 10
    # S = 11
    # S = 12
    # S = 13
    # S = 14
    # S = 15
    # S = 16
    # S = 17
    # S = 18
    # S = 19
    # S = 20
    # S = 21
    # S = 22
    # S = 23
    # S = 24
    # S = 25
    # S = 26
    # S = 27
    # S = 28
    # S = 29
    # S = 30
    # S = 31
    # S = 32
    # S = 33
    # S = 34
    # S = 35
    # S = 36
    # S = 37
    # S = 38
    # S = 39
    # S = 40
    # S = 41
    # S = 42
    # S = 43
    # S = 44
    # S = 45
    # S = 46
    # S = 47
    # S = 48
    # S = 49
    # S = 50
    # S = 51
    # S = 52
    # S = 53
    # S = 54
    # S = 55
    # S = 56
    # S = 57
    # S = 58
    # S = 59
    # S = 60
    # S = 61
    # S = 62
    # S = 63
    # S = 64
    # S = 65
    # S

=======
Suggestion 3

def main():
    S = input()
    S = S[::-1]
    N = len(S)
    dp = [[0 for _ in range(2)] for _ in range(N+1)]
    dp[0][0] = 0
    dp[0][1] = 1
    for i in range(N):
        for j in range(2):
            if j == 0:
                dp[i+1][0] = min(dp[i][0]+int(S[i]),dp[i][1]+10-int(S[i]))
                dp[i+1][1] = min(dp[i][0]+int(S[i])+1,dp[i][1]+9-int(S[i]))
            else:
                dp[i+1][0] = min(dp[i][0]+int(S[i])+1,dp[i][1]+10-int(S[i]))
                dp[i+1][1] = min(dp[i][0]+int(S[i])+2,dp[i][1]+9-int(S[i]))
    print(dp[N][0])

=======
Suggestion 4

def solve():
    # n = int(input())
    # a = list(map(int, input().split()))
    s = int(input())
    # s = input()
    # h, w = map(int, input().split())
    # a = [list(map(int, input().split())) for _ in range(h)]
    # b = [int(input()) for _ in range(n)]
    # print(s)
    # print(len(s))
    # print(s[0])
    # print(s[1])
    # print(s[2])
    # print(s[3])
    # print(s[4])
    # print(s[5])
    # print(s[6])
    # print(s[7])
    # print(s[8])
    # print(s[9])
    # print(s[10])
    # print(s[11])
    # print(s[12])
    # print(s[13])
    # print(s[14])
    # print(s[15])
    # print(s[16])
    # print(s[17])
    # print(s[18])
    # print(s[19])
    # print(s[20])
    # print(s[21])
    # print(s[22])
    # print(s[23])
    # print(s[24])
    # print(s[25])
    # print(s[26])
    # print(s[27])
    # print(s[28])
    # print(s[29])
    # print(s[30])
    # print(s[31])
    # print(s[32])
    # print(s[33])
    # print(s[34])
    # print(s[35])
    # print(s[36])
    # print(s[37])
    # print(s[38])
    # print(s[39])
    # print(s[40])
    # print(s[41])
    # print(s[42])
    # print(s[43])
    # print(s[44])
    # print(s[45])
    # print(s[46])
    # print(s[47])
    # print(s[48])
    # print(s[49])
    # print(s[50])
    # print(s[51])
    # print(s[52])
    # print(s[53])
    # print(s[54])
    # print(s[55])
    # print(s[56])
    # print(s[57])
    # print(s

=======
Suggestion 5

def main():
    S = input()
    ans = 0
    for i in range(len(S)):
        if S[i] == '0':
            continue
        ans += int(S[i])
        ans += 10 ** (len(S) - i - 1) - 1
    print(ans)
    return

=======
Suggestion 6

def solve(s):
    ans = 0
    while s:
        if s[-1] == '0':
            s = s[:-1]
            ans += 1
        else:
            s = str(int(s) - 1)
            ans += 1
    return ans

s = input()
print(solve(s))

=======
Suggestion 7

def main():
    S = input()
    #print(S)
    #print(len(S))
    s_len = len(S)
    #print(s_len)
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
    #print(S[64])
    #print(S[65])
    #print(S[66])

=======
Suggestion 8

def main():
    # input
    S = input()

    # compute
    cnt = 0
    for i in range(len(S)-1):
        if S[i] == '0':
            cnt += 1
    if S[-1] == '0':
        cnt += 1
    else:
        cnt += int(S[-1])

    # output
    print(cnt)

=======
Suggestion 9

def main():
    S = input()
    N = len(S)
    dp = [[0, 0] for i in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(2):
            if j == 1:
                dp[i + 1][j] += dp[i][j] * 8
            else:
                dp[i + 1][j] += dp[i][j]
                if S[i] == "1":
                    dp[i + 1][j + 1] += dp[i][j]
                elif S[i] != "0":
                    dp[i + 1][j] += dp[i][j]
                else:
                    dp[i + 1][j + 1] += dp[i][j]
    print(dp[N][0] + dp[N][1])

=======
Suggestion 10

def main():
    S = input()
    #print(S)
    #print(type(S))
    #print(len(S))
    #print(S[0])
    #print(S[1])
    #print(S[-1])
    #print(S[-2])
    #print(S[-3])
    #print(S[-4])
    #print(S[-5])
    #print(S[-6])
    #print(S[-7])
    #print(S[-8])
    #print(S[-9])
    #print(S[-10])
    #print(S[-11])
    #print(S[-12])
    #print(S[-13])
    #print(S[-14])
    #print(S[-15])
    #print(S[-16])
    #print(S[-17])
    #print(S[-18])
    #print(S[-19])
    #print(S[-20])
    #print(S[-21])
    #print(S[-22])
    #print(S[-23])
    #print(S[-24])
    #print(S[-25])
    #print(S[-26])
    #print(S[-27])
    #print(S[-28])
    #print(S[-29])
    #print(S[-30])
    #print(S[-31])
    #print(S[-32])
    #print(S[-33])
    #print(S[-34])
    #print(S[-35])
    #print(S[-36])
    #print(S[-37])
    #print(S[-38])
    #print(S[-39])
    #print(S[-40])
    #print(S[-41])
    #print(S[-42])
    #print(S[-43])
    #print(S[-44])
    #print(S[-45])
    #print(S[-46])
    #print(S[-47])
    #print(S[-48])
    #print(S[-49])
    #print(S[-50])
    #print(S[-51])
    #print(S[-52])
    #print(S[-53])
    #print(S[-54])
    #print(S[-55])
    #print(S[-56])
    #print(S[-57])
    #print(S[-58])
    #print(S[-59])
    #print(S[-60])
    #print(S[-61])
    #print(S[-62])
    #print(S[-63])
    #print(S[-64])
    #print(S[-65])
    #print(S[-66])
