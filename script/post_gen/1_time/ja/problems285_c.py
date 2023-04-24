Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    n = len(s)
    ans = 0
    for i in range(n):
        ans += (ord(s[i]) - ord('A') + 1) * (26 ** (n - 1 - i))
    print(ans)

=======
Suggestion 2

def main():
    s = input()
    n = len(s)
    ans = 0
    for i in range(n):
        ans += 26 ** (n - i - 1) * (ord(s[i]) - ord('A') + 1)
    print(ans)

=======
Suggestion 3

def main():
    S = input()
    ans = 0
    for i in range(len(S)):
        ans += 26**i * (ord(S[i]) - ord('A') + 1)
    print(ans)

=======
Suggestion 4

def main():
    s = input()
    n = len(s)
    ans = 0
    for i in range(n):
        ans += (ord(s[i])-64) * 26**(n-i-1)
    print(ans)

=======
Suggestion 5

def main():
    s = input()
    n = len(s)
    ans = 0
    for i in range(n-1):
        ans += 26**(i+1)
    ans += ord(s[0]) - ord('A') + 1
    for i in range(1,n):
        ans += (ord(s[i]) - ord('A')) * 26**(n-i)
    print(ans)

=======
Suggestion 6

def main():
    S = input()
    print(26**(len(S)-1)*(ord(S[0])-64)+sum([26**(len(S)-i-1)*(ord(S[i])-64) for i in range(1,len(S))]))

=======
Suggestion 7

def main():
    S = input()
    ans = 0
    for i in range(len(S)):
        ans += (26 ** (i)) * (ord(S[len(S) - 1 - i]) - 64)
    print(ans)

=======
Suggestion 8

def main():
    S = input()
    l = len(S)
    ans = 0
    for i in range(l):
        ans += 26**i
    ans += sum([ord(s) - ord("A") + 1 for s in S]) - l
    print(ans)

=======
Suggestion 9

def main():
    s = input()
    print(ord(s[0])-ord('A')+1+26*(len(s)-1))

=======
Suggestion 10

def main():
    s = input()
    print((ord(s[0])-64)*26**len(s) + (ord(s[1])-64) if len(s)==2 else ord(s[0])-64)
