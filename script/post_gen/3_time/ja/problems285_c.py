Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    S = input()
    ans = 0
    for i in range(len(S)):
        ans += (ord(S[i]) - 64) * (26 ** (len(S) - i - 1))
    print(ans)

=======
Suggestion 2

def main():
    S = input()
    ans = 0
    for i in range(len(S)):
        if i == 0:
            ans += (ord(S[i])-64)
        else:
            ans += (ord(S[i])-64) * (26**i)
    print(ans)

=======
Suggestion 3

def main():
    s = input()
    ans = 0
    for i in range(len(s)):
        ans += (ord(s[i])-64)*(26**(len(s)-i-1))
    print(ans)

=======
Suggestion 4

def main():
    s = input()
    n = len(s)
    ans = 0
    for i in range(n):
        ans += (ord(s[i])-ord('A'))*(26**(n-i-1))
    print(ans+1)

=======
Suggestion 5

def main():
    s = input()
    ans = 0
    for i in range(len(s)):
        ans += (ord(s[i])-ord('A')+1)*26**(len(s)-1-i)
    print(ans)

=======
Suggestion 6

def main():
    s = input()
    n = len(s)
    ans = 0

    for i in range(n):
        ans += (ord(s[i]) - ord('A')) * pow(26, n - i - 1)

    print(ans + 1)

=======
Suggestion 7

def main():
    s = input()
    i = 0
    n = 0
    while i < len(s):
        if i == 0:
            n += (ord(s[i])-64)
        else:
            n += (ord(s[i])-64) * (26**i)
        i += 1
    print(n)

=======
Suggestion 8

def main():
    S = input()
    #print(S)
    #print(len(S))
    #print(ord('A'))
    #print(ord('Z'))
    #print(ord('A')-64)
    #print(ord('Z')-64)
    #print(ord('A')-64+(ord('A')-64)*26+(ord('A')-64)*26*26)
    #print(ord('B')-64+(ord('A')-64)*26+(ord('A')-64)*26*26)
    #print(ord('C')-64+(ord('A')-64)*26+(ord('A')-64)*26*26)
    #print(ord('Z')-64+(ord('A')-64)*26+(ord('A')-64)*26*26)
    #print(ord('A')-64+(ord('A')-64)*26+(ord('A')-64)*26*26+(ord('A')-64)*26*26*26)
    #print(ord('B')-64+(ord('A')-64)*26+(ord('A')-64)*26*26+(ord('A')-64)*26*26*26)
    #print(ord('C')-64+(ord('A')-64)*26+(ord('A')-64)*26*26+(ord('A')-64)*26*26*26)
    #print(ord('Z')-64+(ord('A')-64)*26+(ord('A')-64)*26*26+(ord('A')-64)*26*26*26)
    #print(ord('A')-64+(ord('A')-64)*26+(ord('A')-64)*26*26+(ord('A')-64)*26*26*26+(ord('A')-64)*26*26*26*26)
    #print(ord('B')-64+(ord('A')-64)*26+(ord('A')-64)*26*26+(ord('A')-64)*26*26*26+(ord('A')-64)*26*26*26*26)
    #print(ord('C')-64+(ord('A')-64)*26+(ord('A')-64)*26*26+(ord('A')-64)*26*26

=======
Suggestion 9

def main():
    S = input()
    #print(S)
    #print(len(S))
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
    #print(ord(S[59]))
    #
