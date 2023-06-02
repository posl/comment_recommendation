Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    n = len(s)
    # dp[i] 表示前i个字符构成的数字除以2019的余数
    dp = [0] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        dp[i] = (dp[i - 1] * 10 + int(s[i - 1])) % 2019
    # print(dp)
    cnt = [0] * 2019
    for i in range(n + 1):
        cnt[dp[i]] += 1
    # print(cnt)
    ans = 0
    for i in range(2019):
        ans += cnt[i] * (cnt[i] - 1) // 2
    print(ans)

=======
Suggestion 2

def main():
    s = input()
    n = len(s)
    ans = 0
    for i in range(n):
        for j in range(i+3,n):
            if int(s[i:j+1])%2019==0:
                ans += 1
    print(ans)
main()

=======
Suggestion 3

def main():
    s = input()
    print(s)

=======
Suggestion 4

def main():
    s = input()
    count = 0
    for i in range(len(s)):
        for j in range(i+3,len(s)):
            if int(s[i:j+1])%2019 == 0:
                count +=1
    print(count)

=======
Suggestion 5

def main():
    s = input()
    s = s[::-1]
    n = len(s)
    mod = 2019
    cnt = [0]*mod
    cnt[0] = 1
    d = 1
    ans = 0
    for i in range(n):
        d = (d*10)%mod
        ans += cnt[d]
        cnt[d] += 1
    print(ans)
main()

=======
Suggestion 6

def main():
    s = input()
    #print(s)
    #print(len(s))
    #print(type(s))
    #print(s[0:2])
    #print(s[2:4])
    #print(s[4:6])
    #print(s[6:8])
    #print(s[8:10])
    #print(s[10:12])
    #print(s[12:14])
    #print(s[14:16])
    #print(s[16:18])
    #print(s[18:20])
    #print(s[20:22])
    #print(s[22:24])
    #print(s[24:26])
    #print(s[26:28])
    #print(s[28:30])
    #print(s[30:32])
    #print(s[32:34])
    #print(s[34:36])
    #print(s[36:38])
    #print(s[38:40])
    #print(s[40:42])
    #print(s[42:44])
    #print(s[44:46])
    #print(s[46:48])
    #print(s[48:50])
    #print(s[50:52])
    #print(s[52:54])
    #print(s[54:56])
    #print(s[56:58])
    #print(s[58:60])
    #print(s[60:62])
    #print(s[62:64])
    #print(s[64:66])
    #print(s[66:68])
    #print(s[68:70])
    #print(s[70:72])
    #print(s[72:74])
    #print(s[74:76])
    #print(s[76:78])
    #print(s[78:80])
    #print(s[80:82])
    #print(s[82:84])
    #print(s[84:86])
    #print(s[86:88])
    #print(s[88:90])
    #print(s[90:92])
    #print(s[92:94])
    #print(s[94:96])
    #print(s[96:98])
    #print(s[98:100])
    #print(s[100:102])
    #print(s[102:104])
    #print(s[104:106

=======
Suggestion 7

def main():
    s = input()
    n = len(s)
    cnt = 0
    for i in range(n):
        for j in range(i, n):
            if int(s[i:j+1]) % 2019 == 0:
                cnt += 1
    print(cnt)

=======
Suggestion 8

def main():
    S = input()
    #print(S)
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
    #print(S[64])
    #print(S[65])
    #print(S[66])
    #print(S[67])
    #print(S[68

=======
Suggestion 9

def main():
    s = input()
    n = len(s)
    a = [0]*2019
    a[0] = 1
    t = 0
    ans = 0
    for i in range(n-1, -1, -1):
        t += int(s[i])*pow(10, n-1-i, 2019)
        t %= 2019
        ans += a[t]
        a[t] += 1
    print(ans)

=======
Suggestion 10

def main():
    S = input()
    N = len(S)
    S = S[::-1]
    # T = [0] * (N + 1)
    # for i in range(N):
    #     T[i + 1] = (T[i] + int(S[i]) * pow(10, i, 2019)) % 2019
    # print(T)
    # print(S)
    # print(N)
    # print(S[0])
    # print(int(S[0]))
    # print(pow(10, 0, 2019))
    # print(int(S[0]) * pow(10, 0, 2019))
    # print(T[1])
    # print(T[2])
    # print(T[3])
    # print(T[4])
    # print(T[5])
    # print(T[6])
    # print(T[7])
    # print(T[8])
    # print(T[9])
    # print(T[10])
    # print(T[11])
    # print(T[12])
    # print(T[13])
    # print(T[14])
    # print(T[15])
    # print(T[16])
    # print(T[17])
    # print(T[18])
    # print(T[19])
    # print(T[20])
    # print(T[21])
    # print(T[22])
    # print(T[23])
    # print(T[24])
    # print(T[25])
    # print(T[26])
    # print(T[27])
    # print(T[28])
    # print(T[29])
    # print(T[30])
    # print(T[31])
    # print(T[32])
    # print(T[33])
    # print(T[34])
    # print(T[35])
    # print(T[36])
    # print(T[37])
    # print(T[38])
    # print(T[39])
    # print(T[40])
    # print(T[41])
    # print(T[42])
    # print(T[43])
    # print(T[44])
    # print(T[45])
    # print(T[46])
    # print(T[47])
    # print(T[48])
    # print(T[49])
    # print(T[50])
    # print(T[51])
    #
