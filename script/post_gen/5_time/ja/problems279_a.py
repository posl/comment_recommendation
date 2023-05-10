Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    print(s.count('vw') + s.count('wv'))

=======
Suggestion 2

def solve():
    S = input()
    count = 0
    for i in range(len(S)):
        if S[i] == "v":
            count += S[i+1:].count("w")
    print(count)
solve()

=======
Suggestion 3

def main():
    s = input()
    count = 0
    for i in range(len(s)-1):
        if s[i] == "v" and s[i+1] == "w":
            count += 1
    print(count*2)

=======
Suggestion 4

def main():
    s = input()
    num = 0
    for i in range(len(s)):
        if s[i] == "w" and i != 0:
            if s[i-1] == "v":
                num += 1
    print(num)

=======
Suggestion 5

def solve():
    S = input()
    ans = 0
    for i in range(len(S)):
        if S[i] == "w":
            ans += i
    print(ans)

=======
Suggestion 6

def problem279_a():
    s = input()
    v = 0
    w = 0
    for i in range(len(s)):
        if s[i] == "v":
            v += 1
        else:
            w += 1
    print(v*w)

=======
Suggestion 7

def solve():
    s = input()
    ans = 0
    for i in range(len(s)-1):
        if s[i] == 'v' and s[i+1] == 'w':
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    s = input()
    l = len(s)
    v = 0
    w = 0
    for i in range(l):
        if s[i] == 'v':
            v += 1
        else:
            w += 1
    print(v*w)

=======
Suggestion 9

def countSharp(s):
    c = 0
    for i in range(len(s)):
        if s[i] == 'v' and i < len(s) - 1 and s[i+1] == 'w':
            c += 1
    return c

=======
Suggestion 10

def main():
    s = input()
    print(s.count("vv") + s.count("ww"))
