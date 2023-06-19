Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n = int(input())
    c = input()
    ans = 0
    w = 0
    for i in range(n):
        if c[i] == 'W':
            w += 1
    for i in range(n):
        if i < w and c[i] == 'R':
            ans += 1
    print(ans)
solve()

=======
Suggestion 2

def solve():
    N = int(input())
    S = input()
    cnt = 0
    w_cnt = 0
    for i in range(N):
        if S[i] == 'W':
            w_cnt += 1
        else:
            cnt += w_cnt
    print(cnt)

solve()

=======
Suggestion 3

def solve(n, c):
    w = c.count('W')
    r = c.count('R')
    if w == 0 or r == 0:
        return 0
    if w == r:
        return 1
    if w > r:
        return r
    if w < r:
        return w

=======
Suggestion 4

def solve(n, c):
    if n == 1:
        return 1 if c == 'W' else 0
    if n == 2:
        return 1 if c == 'R' else 0
    cnt = 0
    if c == 'W':
        cnt += 1
    for i in range(1, n):
        if c == 'R':
            if i % 2 == 0:
                cnt += 1
        else:
            if i % 2 == 1:
                cnt += 1
    return cnt

=======
Suggestion 5

def solve(n,c):
    r = 0
    w = 0
    for i in range(n):
        if c[i] == 'R':
            r += 1
    for i in range(r):
        if c[i] == 'W':
            w += 1
    return w

=======
Suggestion 6

def main():
    n = int(input())
    s = input()
    r = 0
    w = 0
    for i in range(n):
        if s[i] == 'R':
            r += 1
    for i in range(r):
        if s[i] == 'W':
            w += 1
    print(w)

=======
Suggestion 7

def main():
    N = int(input())
    c = input()
    left = 0
    right = N - 1
    count = 0
    while left < right:
        if c[left] == 'W' and c[right] == 'R':
            count += 1
            left += 1
            right -= 1
        elif c[left] == 'R':
            left += 1
        elif c[right] == 'W':
            right -= 1
    print(count)

=======
Suggestion 8

def main():
    N = int(input())
    c = input()
    count = 0
    # 先把W移到最左边
    for i in range(N):
        if c[i] == 'W':
            count += 1
    print(count)

=======
Suggestion 9

def main():
    n = int(input())
    c = input()
    r, w = 0, 0
    for i in range(n):
        if c[i] == "R":
            r += 1
    for i in range(r):
        if c[i] == "W":
            w += 1
    print(w)

=======
Suggestion 10

def solve():
    n = int(input())
    s = input()
    r = s.count("R")
    w = s.count("W")
    if r == 0 or w == 0:
        return 0
    if r == w:
        return 0
    if r > w:
        return w
    else:
        return r
print(solve())
