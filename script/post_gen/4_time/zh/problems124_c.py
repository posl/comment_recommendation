Synthesizing 10/10 solutions

=======
Suggestion 1

def minPaint(N, S):
    count = 0
    for i in range(0, N-1):
        if S[i] == S[i+1]:
            count += 1
    return count

=======
Suggestion 2

def main():
    s = input()
    count = 0
    for i in range(len(s)):
        if s[i] == '0':
            count += 1
    print(min(count, len(s) - count))

=======
Suggestion 3

def solve(s):
    #print(s)
    if len(s) <= 1:
        return 0
    if len(s) == 2:
        if s[0] == s[1]:
            return 1
        else:
            return 0

    count = 0
    if s[0] == s[1]:
        if s[0] == '0':
            count += 1
            s = '1' + s[1:]
        else:
            count += 1
            s = '0' + s[1:]

    for i in range(1, len(s) - 1):
        if s[i] == s[i + 1]:
            if s[i] == '0':
                count += 1
                s = s[:i + 1] + '1' + s[i + 2:]
            else:
                count += 1
                s = s[:i + 1] + '0' + s[i + 2:]

    if s[-1] == s[-2]:
        if s[-1] == '0':
            count += 1
            s = s[:-1] + '1'
        else:
            count += 1
            s = s[:-1] + '0'

    #print(s)
    return count + solve(s)

=======
Suggestion 4

def main():
    s = input()
    n = len(s)
    count = 0
    for i in range(n):
        if i % 2 == 0 and s[i] == '1':
            count += 1
        elif i % 2 == 1 and s[i] == '0':
            count += 1
    print(min(count, n - count))

=======
Suggestion 5

def main():
    s = input()
    num = 0
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] == '1':
                num += 1
        else:
            if s[i] == '0':
                num += 1
    print(num)

=======
Suggestion 6

def main():
    S = input()
    N = len(S)
    cnt = 0
    for i in range(N):
        if (i % 2 == 0 and S[i] == '1') or (i % 2 == 1 and S[i] == '0'):
            cnt += 1
    print(min(cnt, N - cnt))

=======
Suggestion 7

def main():
    s = input()
    #print(s)
    #print(len(s))
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
    #print(s[68

=======
Suggestion 8

def main():
    s = input()
    #print(s)
    count = 0
    for i in range(len(s)):
        if i%2 == 0 and s[i] == '1':
            count += 1
        elif i%2 == 1 and s[i] == '0':
            count += 1
    print(min(count, len(s)-count))

=======
Suggestion 9

def solve(s):
    if len(s) == 1:
        return 0
    else:
        count = 0
        if s[0] == s[1]:
            count += 1
            if s[0] == '0':
                s[0] = '1'
            else:
                s[0] = '0'
        for i in range(1, len(s)-1):
            if s[i] == s[i+1] or s[i] == s[i-1]:
                count += 1
                if s[i] == '0':
                    s[i] = '1'
                else:
                    s[i] = '0'
        if s[-1] == s[-2]:
            count += 1
            if s[-1] == '0':
                s[-1] = '1'
            else:
                s[-1] = '0'
        return count

=======
Suggestion 10

def problem124_c():
    s = input()
    s1 = s.replace('0', ' ')
    s2 = s1.split()
    s3 = s.replace('1', ' ')
    s4 = s3.split()
    if len(s2) > len(s4):
        print(len(s4))
    else:
        print(len(s2))
