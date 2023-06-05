Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    c = input()
    r = c.count('R')
    w = c.count('W')
    if r == 0 or w == 0:
        print(0)
        return
    cr = c.count('R', 0, r)
    cw = c.count('W', r, N)
    print(min(cr, cw) + abs(r - w))

=======
Suggestion 2

def main():
    n = int(input())
    c = input()
    r = c.count('R')
    w = c.count('W')
    if r == 0 or w == 0:
        print(0)
    else:
        print(min(r, w) + (r - min(r, w)) // 2)

=======
Suggestion 3

def solve():
    n = int(input())
    s = input()
    r = s.count('R')
    w = s.count('W')
    if r == 0 or w == 0:
        print(0)
        return

    ans = min(r,w)
    cnt = 0
    for i in range(n):
        if s[i] == 'R':
            cnt += 1
            if cnt > ans:
                break
    print(ans - cnt)

=======
Suggestion 4

def main():
    N = int(input())
    c = input()
    r, w = 0, 0
    for i in range(N):
        if c[i] == 'R':
            r += 1
    ans = 0
    for i in range(r):
        if c[i] == 'W':
            ans += 1
    print(ans)

=======
Suggestion 5

def solve():
    N = int(input())
    c = input()
    c = list(c)
    r = c.count('R')
    w = c.count('W')
    ans = 0
    for i in range(r):
        if c[i] == 'W':
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    c = input()
    c_list = list(c)
    count = 0
    for i in range(N):
        if c_list[i] == 'W':
            count += 1
    print(count)

=======
Suggestion 7

def min_op(s):
    l = len(s)
    r = s.count('R')
    w = s.count('W')
    if r == 0 or w == 0:
        return 0
    if r == w:
        return 2
    if r > w:
        return w
    if w > r:
        return r

=======
Suggestion 8

def main():
    n = int(input())
    c = input()
    r = c.count('R')
    w = c.count('W')
    if r == 0 or w == 0:
        print(0)
    else:
        print(min(r,w))

=======
Suggestion 9

def main():
    n = int(input())
    c = input()
    r = c.count('R')
    w = c.count('W')
    ans = 0
    for i in range(r):
        if c[i] == 'W':
            ans += 1
    print(ans)

=======
Suggestion 10

def solve():
    N = int(input())
    c = input()
    w = c.count('W')
    ans = 0
    for i in range(w):
        if c[i] == 'R':
            ans += 1
    print(ans)
