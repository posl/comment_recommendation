Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    s = input()
    n = len(s)
    r = 0
    b = 0
    for i in range(n):
        if s[i] == '0':
            r += 1
        else:
            b += 1
    print(min(r,b)*2)

=======
Suggestion 2

def solve(S):
    count = 0
    for i in range(len(S)):
        if S[i] == "0":
            count += 1
    return min(count, len(S)-count)*2

=======
Suggestion 3

def solve():
    S = input()
    N = len(S)
    red = 0
    blue = 0
    for i in range(N):
        if S[i] == '0':
            red += 1
        else:
            blue += 1
    print(2 * min(red, blue))

=======
Suggestion 4

def main():
    s = input()
    #s = "11011010001011"
    #s = "0011"
    l = len(s)
    red = 0
    blue = 0
    for i in range(l):
        if s[i] == "0":
            red += 1
        else:
            blue += 1
    print(min(red, blue) * 2)

=======
Suggestion 5

def main():
    S = input()
    N = len(S)
    c = 0
    for i in range(N):
        if S[i] == "0":
            c += 1
        else:
            c -= 1
    print(N - abs(c))

=======
Suggestion 6

def main():
    # 读入数据
    s = input()
    # 初始化
    red = 0
    blue = 0
    # 计算
    for i in range(len(s)):
        if s[i] == "0":
            red += 1
        else:
            blue += 1
    # 输出
    print(min(red, blue) * 2)

=======
Suggestion 7

def main():
    S = input()
    N = len(S)
    #print(S)
    #print(N)
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

=======
Suggestion 8

def main():
    s = input()
    red = 0
    blue = 0
    for i in range(len(s)):
        if s[i] == '0':
            red += 1
        else:
            blue += 1
    print(min(red, blue) * 2)

=======
Suggestion 9

def main():
    s = input()
    print(s.count('0')*2 if s.count('0') < s.count('1') else s.count('1')*2)

=======
Suggestion 10

def main():
    s = input()
    n = len(s)
    ans = 0
    for i in range(n):
        if s[i] == '0':
            ans += 1
    print(min(ans, n-ans)*2)
