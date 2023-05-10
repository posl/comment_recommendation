Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    r = s.count('R')
    w = s.count('W')
    ans = min(r, w)
    rnum = 0
    wnum = 0
    for i in range(n):
        if s[i] == 'R':
            rnum += 1
        else:
            wnum += 1
        ans = min(ans, max(rnum, wnum))
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    c = list(input())
    r = c.count('R')
    w = c.count('W')
    ans = 0
    for i in range(r):
        if c[i] == 'W':
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    c = input()
    r = c.count('R')
    w = c.count('W')
    if r == 0 or w == 0:
        print(0)
        return
    else:
        if c[0] == 'W':
            r = c.count('R', 1)
            w = c.count('W', r)
        else:
            w = c.count('W', 1)
            r = c.count('R', w)
        print(min(r, w))

=======
Suggestion 4

def main():
    n = int(input())
    c = input()
    r = 0
    w = 0
    for i in c:
        if i == 'R':
            r += 1
        else:
            w += 1
    if r == 0 or w == 0:
        print(0)
    elif c[0] == 'R' and c[-1] == 'R':
        print(w)
    elif c[0] == 'W' and c[-1] == 'W':
        print(r)
    else:
        print(1)

=======
Suggestion 5

def main():
    N = int(input())
    c = input()
    r = 0
    w = 0
    for i in range(N):
        if c[i] == 'R':
            r += 1
        else:
            w += 1
    ans = 0
    for i in range(r):
        if c[i] == 'W':
            ans += 1
    print(ans)

=======
Suggestion 6

def solve():
    N = int(input())
    C = input()
    r = 0
    w = 0
    for i in range(N):
        if C[i] == 'R':
            r += 1
        else:
            w += 1
    if r == 0 or w == 0:
        print(0)
        return
    if C[0] == 'R':
        r -= 1
    else:
        w -= 1
    if C[N-1] == 'W':
        w -= 1
    else:
        r -= 1
    print(min(r,w))
    return

=======
Suggestion 7

def main():
    n = int(input())
    s = input()
    r = s.count('R')
    w = s.count('W')
    ans = min(r, w)
    for i in range(ans):
        if s[i] == 'R':
            r -= 1
    ans += r
    print(ans)

=======
Suggestion 8

def solve():
    n = int(input())
    s = input()
    r = s.count('R')
    w = s.count('W')
    ans = min(r, w)
    r = s[:r].count('W')
    w = s[:w].count('R')
    ans = min(ans, max(r, w))
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    c = input()
    r = c.count('R')
    w = n - r
    rw = c[:r].count('W')
    print(rw)

=======
Suggestion 10

def main():
    N = int(input())
    c = input()
    r = 0
    w = 0
    for i in range(N):
        if c[i] == 'R':
            r += 1
    for i in range(r):
        if c[i] == 'W':
            w += 1
    print(w)
