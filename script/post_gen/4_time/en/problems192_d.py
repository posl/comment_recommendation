Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    X = input()
    M = int(input())
    d = max(X)
    if len(X) == 1:
        if int(X) <= M:
            print(1)
        else:
            print(0)
        return

    start, end = int(d) + 1, M + 1
    while end - start > 1:
        mid = (start + end) // 2
        v = 0
        for c in X:
            v = v * mid + int(c)
            if v > M:
                break
        if v <= M:
            start = mid
        else:
            end = mid
    print(start - int(d))

=======
Suggestion 2

def main():
    X = input()
    M = int(input())
    if len(X) == 1:
        if int(X) <= M:
            print(1)
        else:
            print(0)
        exit()
    d = max(X)
    d = int(d)
    l = d + 1
    r = M + 1
    while r - l > 1:
        m = (l + r) // 2
        v = 0
        for i in range(len(X)):
            v = v * m + int(X[i])
            if v > M:
                break
        if v <= M:
            l = m
        else:
            r = m
    print(l - d)

=======
Suggestion 3

def main():
    X = input()
    M = int(input())
    d = 0
    for i in X:
        if int(i) > d:
            d = int(i)
    if len(X) == 1:
        if d <= M:
            print(1)
        else:
            print(0)
        return
    l = d + 1
    r = M + 1
    while r - l > 1:
        m = (l + r) // 2
        val = 0
        for i in X:
            val = val * m + int(i)
            if val > M:
                break
        if val > M:
            r = m
        else:
            l = m
    print(l - d)

=======
Suggestion 4

def main():
    X = input()
    M = int(input())
    d = 0
    for x in X:
        d = max(d, int(x))
    if len(X) == 1:
        print(1 if d <= M else 0)
        return
    left = d
    right = M + 1
    while right - left > 1:
        mid = (left + right) // 2
        if int(X, mid) <= M:
            left = mid
        else:
            right = mid
    print(left - d)

=======
Suggestion 5

def main():
    X = input()
    M = int(input())
    d = int(max(X))
    if len(X) == 1:
        print(1 if d <= M else 0)
        exit()
    l, r = d, M+1
    while r-l > 1:
        m = (l+r)//2
        if int(X, m) <= M:
            l = m
        else:
            r = m
    print(l-d)

=======
Suggestion 6

def solve(x, m):
    d = int(max(x))
    if len(x) == 1:
        if int(x) <= m:
            return 1
        else:
            return 0
    elif d == 1:
        return len(x)
    else:
        l = 0
        r = m + 1
        while r - l > 1:
            mid = (r + l) // 2
            if int(x, mid) <= m:
                l = mid
            else:
                r = mid
        return l - d

x = input()
m = int(input())
print(solve(x, m))

from sys import stdin
from math import log

=======
Suggestion 7

def solve(X, M):
    d = max(X)
    if len(X) == 1:
        if int(X) <= M:
            return 1
        else:
            return 0
    else:
        ans = 0
        for i in range(int(d)+1, M+1):
            n = 0
            for j in range(len(X)):
                n += int(X[j]) * (i ** (len(X)-j-1))
            if n <= M:
                ans += 1
            else:
                break
        return ans

X = input()
M = int(input())
print(solve(X, M))

=======
Suggestion 8

def main():
    X = int(input())
    M = int(input())
    if M < X:
        print(0)
        return
    if X < 10:
        print(1)
        return
    X = str(X)
    d = max(X)
    n = int(d) + 1
    while True:
        if n * (n - 1) ** (len(X) - 1) > M:
            break
        n += 1
    print(n - d - 1)

main()

=======
Suggestion 9

def calc_d(x):
    d = 0
    for i in x:
        if int(i) > d:
            d = int(i)
    return d
