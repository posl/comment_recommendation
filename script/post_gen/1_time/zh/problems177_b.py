Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def min_change_number(s, t):
    s_len = len(s)
    t_len = len(t)
    min_change = s_len
    for i in range(s_len - t_len + 1):
        change = 0
        for j in range(t_len):
            if s[i + j] != t[j]:
                change += 1
        if change < min_change:
            min_change = change
    return min_change

=======
Suggestion 2

def main():
    s = input()
    t = input()
    len_s = len(s)
    len_t = len(t)
    min_change = len_t
    for i in range(len_s - len_t + 1):
        change = 0
        for j in range(len_t):
            if s[i + j] != t[j]:
                change += 1
        if change < min_change:
            min_change = change
    print(min_change)

=======
Suggestion 3

def main():
    s = input()
    t = input()
    ans = len(t)
    for i in range(len(s)-len(t)+1):
        cnt = 0
        for j in range(len(t)):
            if s[i+j] != t[j]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 4

def solve(s,t):
    n = len(s)
    m = len(t)
    dp = [[0]*(m+1) for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s[i-1]==t[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=dp[i-1][j]
    return m-dp[n][m]

s = input()
t = input()
print(solve(s,t))

=======
Suggestion 5

def main():
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
Suggestion 6

def solve():
    s = input()
    t = input()
    min = len(t)
    for i in range(len(s)-len(t)+1):
        count = 0
        for j in range(len(t)):
            if s[i+j] != t[j]:
                count += 1
        if count < min:
            min = count
    print(min)

=======
Suggestion 7

def solve():
    s = input()
    t = input()
    min = len(t)
    for i in range(len(s)-len(t)+1):
        count = 0
        for j in range(len(t)):
            if s[i+j] != t[j]:
                count += 1
        if min > count:
            min = count
    print(min)

=======
Suggestion 8

def main():
    s = input()
    t = input()
    min = len(t)
    for i in range(len(s)-len(t)+1):
        count = 0
        for j in range(len(t)):
            if s[i+j] != t[j]:
                count += 1
        if count < min:
            min = count
    print(min)

=======
Suggestion 9

def main():
    s = input()
    t = input()
    #print(s)
    #print(t)
    #print(len(s))
    #print(len(t))
    #print(s[0:3])
    #print(s[1:4])
    #print(s[2:5])
    #print(s[3:6])
    #print(s[4:7])
    #print(s[5:8])
    #print(s[6:9])
    #print(s[7:10])
    #print(s[8:11])
    #print(s[9:12])
    #print(s[10:13])
    #print(s[11:14])
    #print(s[12:15])
    #print(s[13:16])
    #print(s[14:17])
    #print(s[15:18])
    #print(s[16:19])
    #print(s[17:20])
    #print(s[18:21])
    #print(s[19:22])
    #print(s[20:23])
    #print(s[21:24])
    #print(s[22:25])
    #print(s[23:26])
    #print(s[24:27])
    #print(s[25:28])
    #print(s[26:29])
    #print(s[27:30])
    #print(s[28:31])
    #print(s[29:32])
    #print(s[30:33])
    #print(s[31:34])
    #print(s[32:35])
    #print(s[33:36])
    #print(s[34:37])
    #print(s[35:38])
    #print(s[36:39])
    #print(s[37:40])
    #print(s[38:41])
    #print(s[39:42])
    #print(s[40:43])
    #print(s[41:44])
    #print(s[42:45])
    #print(s[43:46])
    #print(s[44:47])
    #print(s[45:48])
    #print(s[46:49])
    #print(s[47:50])
    #print(s[48:51])
    #print(s[49:52])
    #print(s[50:53])
    #print(s[51:
