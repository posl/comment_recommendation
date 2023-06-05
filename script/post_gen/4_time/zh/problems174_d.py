Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    c = input()
    cnt = 0
    for i in range(n):
        if c[i] == "W":
            cnt += 1
    ans = 0
    for i in range(cnt):
        if c[i] == "R":
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    c = list(input())
    r = c.count('R')
    w = c.count('W')
    if r == 0 or w == 0:
        print(0)
        return
    if c[0] == 'R':
        print(w)
    else:
        print(r)

=======
Suggestion 3

def main():
    N = int(input())
    c = input()
    w = c.count('W')
    r = c.count('R')
    if w == 0 or r == 0:
        print(0)
        return
    w1 = 0
    r1 = 0
    for i in range(N):
        if c[i] == 'W':
            w1 += 1
        else:
            r1 += 1
        if w1 == r:
            print(r1)
            return

=======
Suggestion 4

def solve():
    pass

=======
Suggestion 5

def main():
    n = int(input())
    colors = list(input())
    left = 0
    right = n - 1
    count = 0
    while left < right:
        if colors[left] == 'W':
            while left < right and colors[right] == 'W':
                right -= 1
            if left < right:
                colors[left], colors[right] = colors[right], colors[left]
                count += 1
                left += 1
                right -= 1
        else:
            left += 1
    print(count)

=======
Suggestion 6

def main():
    n = int(input())
    s = input()
    r = s.count("R")
    w = s.count("W")
    if r == 0 or w == 0:
        print(0)
        return
    if r == w:
        print(r)
        return
    if r > w:
        print(w)
        return
    if r < w:
        print(r)
        return

=======
Suggestion 7

def solve():
    n = int(input())
    s = input()
    left = 0
    right = n - 1
    ans = 0
    while True:
        while left < n and s[left] == 'R':
            left += 1
        while right >= 0 and s[right] == 'W':
            right -= 1
        if left >= right:
            break
        ans += 1
        left += 1
        right -= 1
    print(ans)

=======
Suggestion 8

def solution():
    n = int(input())
    s = input()
    w = 0
    r = 0
    for i in range(n):
        if s[i] == 'W':
            w += 1
        else:
            r += 1
    if w == 0 or r == 0:
        print(0)
        return
    if s[0] == 'R' and s[-1] == 'R':
        print(r - 1)
        return
    if s[0] == 'W' and s[-1] == 'W':
        print(w - 1)
        return
    if s[0] == 'W' and s[-1] == 'R':
        print(r)
        return
    if s[0] == 'R' and s[-1] == 'W':
        print(r)
        return
    print(min(r, w))

=======
Suggestion 9

def main():
    n = int(input())
    c = input()
    l = 0
    r = n-1
    ans = 0
    while l < r:
        if c[l] == 'W':
            if c[r] == 'R':
                ans += 1
                l += 1
                r -= 1
            else:
                r -= 1
        else:
            l += 1
    print(ans)

=======
Suggestion 10

def solve(n, c):
    # i番目以前有几个W
    w = [0] * (n + 1)
    for i in range(n):
        w[i + 1] = w[i] + (1 if c[i] == 'W' else 0)
    # i番目以后有几个R
    r = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        r[i] = r[i + 1] + (1 if c[i] == 'R' else 0)
    return max(w[i] + r[i] for i in range(n + 1))
