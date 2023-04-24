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
    left = d
    right = M + 1
    while right - left > 1:
        mid = (left + right) // 2
        value = 0
        for i in range(len(X)):
            value = value * mid + int(X[i])
        if value <= M:
            left = mid
        else:
            right = mid
    print(left - d)

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

    ng = d
    ok = M + 1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if mid ** len(X) <= M:
            ng = mid
        else:
            ok = mid
    print(ng - d)

=======
Suggestion 3

def main():
    X = input()
    M = int(input())
    d = int(max(X))
    if len(X) == 1:
        if d > M:
            print(0)
        else:
            print(1)
        return
    l = d
    r = M + 1
    while r - l > 1:
        mid = (r + l) // 2
        if int(X, mid) <= M:
            l = mid
        else:
            r = mid
    print(l - d)

=======
Suggestion 4

def main():
    X = input()
    M = int(input())
    if len(X) == 1:
        if int(X) <= M:
            print(1)
        else:
            print(0)
        return
    X = [int(x) for x in X]
    d = max(X)
    left = d
    right = 10**18+1
    while right - left > 1:
        mid = (right + left) // 2
        if check(X, M, mid):
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
        print(1 if int(X) <= M else 0)
        return
    ok = d
    ng = 10 ** 18 + 1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if int(X, mid) <= M:
            ok = mid
        else:
            ng = mid
    print(ok - d)

=======
Suggestion 6

def main():
    X = input()
    M = int(input())
    d = max([int(i) for i in list(X)])
    if len(X) == 1:
        if d > M:
            print(0)
        else:
            print(1)
        return
    l = d
    r = M+1
    while r-l > 1:
        m = (r+l)//2
        if int(X, m) <= M:
            l = m
        else:
            r = m
    print(l-d)

=======
Suggestion 7

def main():
    X = input()
    M = int(input())
    lenX = len(X)
    d = int(max(X))
    if lenX == 1:
        if d <= M:
            print(1)
        else:
            print(0)
        return
    left = d
    right = M+1
    while left + 1 < right:
        mid = (left + right) // 2
        if check(X, M, mid):
            left = mid
        else:
            right = mid
    print(left-d)

=======
Suggestion 8

def main():
    X = input()
    M = int(input())
    d = max(X)
    d = int(d) + 1
    if len(X) == 1:
        if int(X) <= M:
            print(1)
        else:
            print(0)
        return
    l = 0
    r = M
    while r - l > 1:
        m = (l + r) // 2
        t = 0
        for i in range(len(X)):
            t *= d
            t += int(X[i])
            if t > M:
                break
        if t <= M:
            l = m
        else:
            r = m
    print(l - d + 1)

=======
Suggestion 9

def main():
    X = input()
    M = int(input())
    X = list(X)
    X = list(map(int, X))
    X.sort(reverse=True)
    d = X[0]
    X = list(map(str, X))
    X = "".join(X)
    X = int(X)
    if d+1 > M:
        print(1)
    else:
        left = d+1
        right = M+1
        while right - left > 1:
            mid = (left + right) // 2
            if mid**len(str(X)) > M:
                right = mid
            else:
                left = mid
        print(left-d)
