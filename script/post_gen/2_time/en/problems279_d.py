Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    g = 1
    t = 0
    while A/((g+1)**0.5) > A/(g**0.5) + B:
        g += 1
        t += B
    t += A/((g)**0.5)
    print(t)

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    if A <= B:
        print(A)
    else:
        lo = 0
        hi = 10 ** 9
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if mid * (mid + 1) // 2 <= A // B:
                lo = mid
            else:
                hi = mid
        ans = hi + (A - B * hi * (hi + 1) // 2) ** 0.5
        print(ans)

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    if A <= B:
        print(A)
        return
    # A > B
    g = 1
    t = 0
    while True:
        t += B
        g += 1
        if A <= t + (A / (g ** 0.5)):
            print(t + (A / (g ** 0.5)))
            return

main()

import math
A,B=map(int,input().split())

=======
Suggestion 4

def main():
    a,b = map(int,input().split())
    g = 1
    t = 0
    while True:
        if a/g**0.5 <= t:
            print(t)
            return
        t += b
        g += 1

main()

=======
Suggestion 5

def main():
    a,b = map(int, input().split())
    g = 1
    t = 0
    while True:
        if a/(g**0.5) < b:
            break
        else:
            g += 1
            t += b
    print(t + a/(g**0.5))

=======
Suggestion 6

def main():
    a, b = map(int, input().split())

    if a < b:
        print(a)
        return

    x = int(a ** 0.5)
    if x * (x + 1) < a:
        x += 1

    ans = 10 ** 18
    for i in range(x):
        ans = min(ans, (a + i) / (x + i))

    print(ans)

=======
Suggestion 7

def main():
    A,B = map(int, input().split())
    t = 0
    while A > 0:
        t += 1
        A -= B
        if A <= 0:
            break
        A = int(A ** 0.5)
    print(t)

=======
Suggestion 8

def main():
    A, B = map(int, input().split())
    def f(g):
        return A / (g ** 0.5)
    def g(t):
        return B * t + f(t)
    def h(t):
        return B * t + f(t + 1)
    def ternary_search(l, r, f):
        while r - l > 10 ** -6:
            c1 = (2 * l + r) / 3
            c2 = (l + 2 * r) / 3
            if f(c1) < f(c2):
                r = c2
            else:
                l = c1
        return f(l)
    print(ternary_search(0, 10 ** 9, g))

=======
Suggestion 9

def main():
    import math
    a,b = map(int,input().split())
    g = 1
    ans = a * (g**(-0.5))
    while True:
        g += 1
        t = b + a * (g**(-0.5))
        if t < ans:
            ans = t
        else:
            break
    print(ans)

=======
Suggestion 10

def main():
    a,b = map(int, input().split())
    print(a**0.5 + (a-1)/b)
