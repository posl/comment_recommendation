Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    ans = 0
    for i in range(len(s)):
        ans += (ord(s[i]) - ord('A') + 1) * 26 ** (len(s) - i - 1)
    print(ans)

=======
Suggestion 2

def main():
    S = input()
    ans = 0
    for i in range(len(S)):
        ans += (ord(S[i]) - ord('A') + 1) * 26 ** (len(S) - i - 1)
    print(ans)

=======
Suggestion 3

def main():
    S = input()
    ans = 0
    for i in range(len(S)):
        ans += (ord(S[i]) - ord('A') + 1) * (26 ** (len(S) - 1 - i))
    print(ans)

=======
Suggestion 4

def main():
    s = input()
    n = len(s)
    ans = 0
    for i in range(n):
        ans += 26 ** (n - i - 1) * (ord(s[i]) - ord("A") + 1)
    print(ans)

=======
Suggestion 5

def main():
    s = input()
    ans = 0
    for i in range(len(s)):
        ans += 26 ** i * (ord(s[i]) - ord('A') + 1)
    print(ans)

=======
Suggestion 6

def main():
    s = input()
    ans = 0
    for i in range(len(s)):
        ans += (ord(s[i])-ord('A')+1)*(26**(len(s)-1-i))
    print(ans)

=======
Suggestion 7

def main():
    s = input()
    l = len(s)
    ans = 0
    for i in range(l):
        ans += 26**i
    ans += ord(s[0])-ord('A')
    for i in range(1,l):
        ans += (ord(s[i])-ord('A'))*26**(l-i)
    print(ans+1)

=======
Suggestion 8

def main():
    s = input()
    l = len(s)
    ans = 0
    for i in range(l):
        ans += 26 ** i
    ans += sum([ord(s[i]) - ord('A') for i in range(l)]) * 26 ** (l - 1) + 1
    print(ans)

=======
Suggestion 9

def main():
    s = input()
    n = len(s)
    ans = 26**(n-1)
    ans += sum([26**i*(ord(s[i])-ord('A')+1) for i in range(n)])
    print(ans)
