Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    X = input()
    M = int(input())
    d = int(max(X))
    if len(X) == 1:
        if d <= M:
            print(1)
        else:
            print(0)
        return
    l = 0
    r = M + 1
    while r - l > 1:
        m = (l + r) // 2
        if int(X, m) <= M:
            l = m
        else:
            r = m
    if d + 1 <= l:
        print(l - d)
    else:
        print(0)

=======
Suggestion 2

def main():
    X = input()
    M = int(input())
    d = int(max(X))
    if len(X) == 1:
        if d <= M:
            print(1)
        else:
            print(0)
        return
    # d+1 <= n <= 10^18
    # n <= 10^18
    # n <= 10^18 - 1
    # n <= 10^18 - 2
    # n <= 10^18 - 3
    # ...
    # n <= 10^18 - d
    # n <= 10^18 - (d+1)
    # n <= 10^18 - (d+2)
    # n <= 10^18 - (d+3)
    # ...
    # n <= 10^18 - (d+d)
    # n <= 10^18 - (d+d+1)
    # ...
    # n <= 10^18 - (d+d+d)
    # n <= 10^18 - (d+d+d+1)
    # ...
    # n <= 10^18 - (d+d+d+d)
    # n <= 10^18 - (d+d+d+d+1)
    # ...
    # n <= 10^18 - (d+d+d+d+d)
    # n <= 10^18 - (d+d+d+d+d+1)
    # ...
    # n <= 10^18 - (d+d+d+d+d+d)
    # n <= 10^18 - (d+d+d+d+d+d+1)
    # ...
    # n <= 10^18 - (d+d+d+d+d+d+d)
    # n <= 10^18 - (d+d+d+d+d+d+d+1)
    # ...
    # n <= 10^18 - (d+d+d+d+d+d+d+d)
    # n <= 10^18 - (d+d+d+d+d+d+d+d+1)
    # ...
    # n <= 10^18 - (d+d+d+d+d+d+d+d+d)
    # n <= 10^18 - (d+d+d+d+d+d+d+d+d+1)
    # ...
    # n <= 10^18 - (d+d+d+d+d+d+d+d+d+d)
    # n <= 10^

=======
Suggestion 3

def main():
    X = input()
    M = int(input())
    d = int(max(X))
    if len(X) == 1:
        if d <= M:
            print(1)
        else:
            print(0)
        return
    l = d + 1
    r = 10**18 + 1
    while r - l > 1:
        m = (l + r) // 2
        if check(X, M, m):
            l = m
        else:
            r = m
    print(l - d)

=======
Suggestion 4

def main():
    X = input()
    M = int(input())
    d = int(max(X))
    if len(X) == 1:
        if d <= M:
            print(1)
        else:
            print(0)
        return
    l = 0
    r = M + 1
    while r - l > 1:
        c = (l + r) // 2
        if d ** len(X) < M:
            l = c
        else:
            r = c
    print(r - d)

=======
Suggestion 5

def main():
    X = input()
    M = int(input())
    d = max([int(x) for x in X])
    if len(X) == 1:
        if d <= M:
            print(1)
        else:
            print(0)
        return
    low = d
    high = M+1
    while high - low > 1:
        mid = (low + high) // 2
        n = 0
        for x in X:
            n = n * mid + int(x)
            if n > M:
                break
        if n > M:
            high = mid
        else:
            low = mid
    print(low - d)

main()

=======
Suggestion 6

def main():
    X = input()
    M = int(input())
    d = 0
    for i in range(len(X)):
        if int(X[i]) > d:
            d = int(X[i])
    if len(X) == 1:
        if int(X) <= M:
            print(1)
        else:
            print(0)
    else:
        l = d
        r = M + 1
        while r - l > 1:
            m = (r + l) // 2
            N = 0
            for i in range(len(X)):
                N = N * m + int(X[i])
            if N <= M:
                l = m
            else:
                r = m
        print(l - d)

=======
Suggestion 7

def solve():
    X = input()
    M = int(input())
    d = max(X)
    d = int(d)
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
        v = 0
        for i in range(len(X)):
            v = v * m + int(X[i])
        if v <= M:
            l = m
        else:
            r = m
    print(l - d)

solve()

=======
Suggestion 8

def main():
    X = input()
    M = int(input())
    d = int(max(X))
    if len(X) == 1:
        print(1 if d <= M else 0)
        return
    x = int(X, d + 1)
    if x <= M:
        print(x - d)
        return
    l, r = d + 1, 10 ** 18
    while r - l > 1:
        m = (l + r) // 2
        if int(X, m) <= M:
            l = m
        else:
            r = m
    print(l - d)

=======
Suggestion 9

def solve():
    X = input()
    M = int(input())
    d = int(max(X))
    n = d + 1
    while True:
        v = 0
        for c in X:
            v = v * n + int(c)
            if v > M:
                break
        if v <= M:
            n += 1
        else:
            break
    print(n - d - 1)
