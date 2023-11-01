Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')

    cnt = 0
    for i in range(n):
        f

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    R = S.count("R")
    G = S.count("G")
    B = S.count("B")
    ans = R * G * B
    for i in range(N):
        for j in

=======
Suggestion 3

def count_rgb(s):
    r = 0
    g = 0
    b = 0
    for c in s:
        if c == 'R':
            r += 1
        elif c == 'G':
            g += 1
        els

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    r = S.count('R')
    g = S.count('G')
    b = S.count('B')
    ans = r * g * b
    for i in range(N):

=======
Suggestion 5

def check(s, i, j, k):
    if s[i] == s[j] or s[i] == s[k] or s[j] == s[k]:
        return False
    if j - i == k - j:
        return False
    return True

=======
Suggestion 6

def main():
    N = int(input())
    S = input()

    # 三重循环
    # count = 0
    # for i in range(N):
    #     for j in range(i + 1, N):
    #         for k

=======
Suggestion 7

def countRGB(s):
    count = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            for k in range(j+1, len(s)):
                if s[i] != s[j] and

=======
Suggestion 8

def solve(n, s):
    r, g, b = 0, 0, 0
    for i in range(n):
        if s[i] == "R":
            r += 1
        elif s[i] == "G":
            g += 1

=======
Suggestion 9

def main():
    n = int(input())
    s = input()
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    ans = r * g * b
    for i in range(n):
        for j in

=======
Suggestion 10

def main():
    n = int(input())
    s = input()
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    total = r * g * b
    for i in range(n):
