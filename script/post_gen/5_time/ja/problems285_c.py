Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    base = 26
    ans = 0
    for i in range(len(s)):
        ans += (ord(s[i]) - ord('A') + 1) * pow(base, len(s) - i - 1)
    print(ans)

=======
Suggestion 2

def main():
    s = input()
    ans = 0
    for i in range(len(s)):
        ans += (ord(s[i]) - 64) * (26 ** (len(s) - 1 - i))
    print(ans)

=======
Suggestion 3

def get_num(s):
    if len(s) == 1:
        return ord(s) - ord('A') + 1
    elif len(s) == 2:
        return (ord(s[0]) - ord('A') + 1)*26 + ord(s[1]) - ord('A') + 1
    elif len(s) == 3:
        return (ord(s[0]) - ord('A') + 1)*26*26 + (ord(s[1]) - ord('A') + 1)*26 + ord(s[2]) - ord('A') + 1
    else:
        return 10000000000000000

=======
Suggestion 4

def get_id(s):
    base = ord('A')
    len_s = len(s)
    max_len = 0
    for i in range(len_s):
        max_len += (26 ** i)
    if len_s == 1:
        return ord(s) - base + 1
    else:
        ans = 0
        for i in range(len_s):
            if i == 0:
                ans += (ord(s[i]) - base) * (26 ** (len_s - i - 1))
            else:
                ans += (ord(s[i]) - base + 1) * (26 ** (len_s - i - 1))
        return ans + max_len

=======
Suggestion 5

def main():
    # input
    S = input()
    # compute
    ans = 0
    for i in range(len(S)):
        ans += (ord(S[i])-ord('A')+1) * 26**(len(S)-i-1)
    # output
    print(ans)

=======
Suggestion 6

def main():
    S = input()
    n = len(S)
    #print(n)
    #print(S)
    #print(ord(S[0]))
    #print(ord(S[1]))
    #print(ord(S[2]))
    #print(ord(S[3]))
    #print(ord(S[4]))
    #print(ord(S[5]))
    #print(ord(S[6]))
    #print(ord(S[7]))
    #print(ord(S[8]))
    #print(ord(S[9]))
    #print(ord(S[10]))
    #print(ord(S[11]))
    #print(ord(S[12]))
    #print(ord(S[13]))
    #print(ord(S[14]))
    #print(ord(S[15]))
    #print(ord(S[16]))
    #print(ord(S[17]))
    #print(ord(S[18]))
    #print(ord(S[19]))
    #print(ord(S[20]))
    #print(ord(S[21]))
    #print(ord(S[22]))
    #print(ord(S[23]))
    #print(ord(S[24]))
    #print(ord(S[25]))
    #print(ord(S[26]))
    #print(ord(S[27]))
    #print(ord(S[28]))
    #print(ord(S[29]))
    #print(ord(S[30]))
    #print(ord(S[31]))
    #print(ord(S[32]))
    #print(ord(S[33]))
    #print(ord(S[34]))
    #print(ord(S[35]))
    #print(ord(S[36]))
    #print(ord(S[37]))
    #print(ord(S[38]))
    #print(ord(S[39]))
    #print(ord(S[40]))
    #print(ord(S[41]))
    #print(ord(S[42]))
    #print(ord(S[43]))
    #print(ord(S[44]))
    #print(ord(S[45]))
    #print(ord(S[46]))
    #print(ord(S[47]))
    #print(ord(S[48]))
    #print(ord(S[49]))
    #print(ord(S[50]))
    #print(ord(S[51]))
    #print(ord(S[52]))
    #print(ord(S[53]))
    #print(ord(S[54]))
    #print(ord(S[55]))
    #print(ord(S[56]))
    #print(ord(S[57]))
    #print(ord(S[58]))
    #print(ord(S

=======
Suggestion 7

def main():
    import sys
    import math
    s = sys.stdin.readline().strip()
    n = len(s)
    if n == 1:
        print(ord(s[0]) - ord('A') + 1)
    elif n == 2:
        print((ord(s[0]) - ord('A') + 1) * 26 + ord(s[1]) - ord('A') + 1)
    elif n == 3:
        print((ord(s[0]) - ord('A') + 1) * 26 * 26 + (ord(s[1]) - ord('A') + 1) * 26 + ord(s[2]) - ord('A') + 1)
    elif n == 4:
        print((ord(s[0]) - ord('A') + 1) * 26 * 26 * 26 + (ord(s[1]) - ord('A') + 1) * 26 * 26 + (ord(s[2]) - ord('A') + 1) * 26 + ord(s[3]) - ord('A') + 1)
    elif n == 5:
        print((ord(s[0]) - ord('A') + 1) * 26 * 26 * 26 * 26 + (ord(s[1]) - ord('A') + 1) * 26 * 26 * 26 + (ord(s[2]) - ord('A') + 1) * 26 * 26 + (ord(s[3]) - ord('A') + 1) * 26 + ord(s[4]) - ord('A') + 1)
    elif n == 6:
        print((ord(s[0]) - ord('A') + 1) * 26 * 26 * 26 * 26 * 26 + (ord(s[1]) - ord('A') + 1) * 26 * 26 * 26 * 26 + (ord(s[2]) - ord('A') + 1) * 26 * 26 * 26 + (ord(s[3]) - ord('A') + 1) * 26 * 26 + (ord(s[4]) - ord('A') + 1) * 26 + ord(s[5]) -

=======
Suggestion 8

def main():
    #文字列を入力
    s = input()
    #長さを取得
    n = len(s)
    #問題数を格納する変数
    cnt = 0
    #1文字の時
    if n == 1:
        cnt = ord(s) - ord("A") + 1
    #2文字の時
    elif n == 2:
        cnt = (ord(s[0]) - ord("A") + 1) * 26 + (ord(s[1]) - ord("A") + 1)
    #3文字の時
    elif n == 3:
        cnt = (ord(s[0]) - ord("A") + 1) * 26 * 26 + (ord(s[1]) - ord("A") + 1) * 26 + (ord(s[2]) - ord("A") + 1)
    #4文字の時
    elif n == 4:
        cnt = (ord(s[0]) - ord("A") + 1) * 26 * 26 * 26 + (ord(s[1]) - ord("A") + 1) * 26 * 26 + (ord(s[2]) - ord("A") + 1) * 26 + (ord(s[3]) - ord("A") + 1)
    #5文字の時
    elif n == 5:
        cnt = (ord(s[0]) - ord("A") + 1) * 26 * 26 * 26 * 26 + (ord(s[1]) - ord("A") + 1) * 26 * 26 * 26 + (ord(s[2]) - ord("A") + 1) * 26 * 26 + (ord(s[3]) - ord("A") + 1) * 26 + (ord(s[4]) - ord("A") + 1)
    #6文字の時
    elif n == 6:
        cnt = (ord(s[0]) - ord("A") + 1) * 26 * 26 * 26 * 26 * 26 + (ord(s[1]) - ord("A") + 1) * 26 * 26 * 26

=======
Suggestion 9

def main():
    s = input()
    n = len(s)
    if n == 1:
        print(ord(s[0]) - 64)
    elif n == 2:
        print(26 + (ord(s[0]) - 64) * 26 + (ord(s[1]) - 64))
    elif n == 3:
        print(26 * 26 + 26 + (ord(s[0]) - 64) * 26 * 26 + (ord(s[1]) - 64) * 26 + (ord(s[2]) - 64))
    elif n == 4:
        print(26 * 26 * 26 + 26 * 26 + 26 + (ord(s[0]) - 64) * 26 * 26 * 26 + (ord(s[1]) - 64) * 26 * 26 + (ord(s[2]) - 64) * 26 + (ord(s[3]) - 64))
    elif n == 5:
        print(26 * 26 * 26 * 26 + 26 * 26 * 26 + 26 * 26 + 26 + (ord(s[0]) - 64) * 26 * 26 * 26 * 26 + (ord(s[1]) - 64) * 26 * 26 * 26 + (ord(s[2]) - 64) * 26 * 26 + (ord(s[3]) - 64) * 26 + (ord(s[4]) - 64))
    elif n == 6:
        print(26 * 26 * 26 * 26 * 26 + 26 * 26 * 26 * 26 + 26 * 26 * 26 + 26 * 26 + 26 + (ord(s[0]) - 64) * 26 * 26 * 26 * 26 * 26 + (ord(s[1]) - 64) * 26 * 26 * 26 * 26 + (ord(s[2]) - 64) * 26 * 26 * 26 + (ord(s[3]) - 64) * 26 * 26 + (ord(s[4]) - 64) * 26 + (ord(s[5]) - 64

=======
Suggestion 10

def main():
    S = input()
    ans = 0
    for i in range(len(S)):
        ans += (ord(S[i])-64) * (26**(len(S)-i-1))
    print(ans)
