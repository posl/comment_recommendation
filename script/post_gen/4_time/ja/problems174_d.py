Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    c = input()
    r = 0
    w = 0
    for i in range(n):
        if c[i] == 'R':
            r += 1
        else:
            w += 1
    ans = min(r, w)
    if ans == 0:
        print(0)
        return
    r = 0
    w = 0
    for i in range(ans):
        if c[i] == 'R':
            r += 1
        else:
            w += 1
    print(ans - min(r, w))

=======
Suggestion 2

def main():
    n = int(input())
    s = input()
    r = 0
    w = 0
    for i in range(n):
        if s[i] == "R":
            r += 1
        else:
            w += 1
    if r == 0 or w == 0:
        print(0)
        exit()
    ans = 0
    for i in range(r):
        if s[i] == "W":
            ans += 1
    print(ans)
main()

=======
Suggestion 3

def main():
    N = int(input())
    C = input()
    r = 0
    w = 0
    for c in C:
        if c == 'R':
            r += 1
        else:
            w += 1
    if r == 0 or w == 0:
        print(0)
        return
    if C[0] == 'W':
        w -= 1
    if C[-1] == 'R':
        r -= 1
    print(min(r, w))

=======
Suggestion 4

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

=======
Suggestion 5

def main():
    N = int(input())
    c = input()
    r = c.count('R')
    w = c.count('W')
    if r == 0 or w == 0:
        print(0)
        return
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
    R = C.count('R')
    W = C.count('W')
    if R == 0 or W == 0:
        print(0)
        return
    r = 0
    w = 0
    for i in range(N):
        if C[i] == 'R':
            r += 1
        else:
            w += 1
        if r >= R or w >= W:
            print(i+1)
            return

=======
Suggestion 7

def main():
    N = int(input())
    c = input()
    count = 0
    r = 0
    w = 0
    for i in range(N):
        if c[i] == "R":
            r += 1
        else:
            w += 1
    for i in range(r):
        if c[i] == "W":
            count += 1
    print(count)

=======
Suggestion 8

def main():
    # input
    N = int(input())
    c = input()
    # compute
    r = c.count('R')
    w = c.count('W')
    # output
    print(min(r, w) + abs(r - w) // 2)

=======
Suggestion 9

def solve():
    N = int(input())
    c = input()
    r = c.count('R')
    w = c.count('W')
    ans = min(r, w)
    r = c[:r].count('W')
    w = c[w:].count('R')
    ans += min(r, w)
    print(ans)

=======
Suggestion 10

def solve():
    N = int(input())
    S = input()
    white = S.count("W")
    red = S.count("R")
    white_count = 0
    red_count = 0
    for i in range(N):
        if S[i] == "W":
            white_count += 1
        else:
            red_count += 1
        if white_count > white - red_count:
            print(red_count)
            return
    print(white_count)
    return
