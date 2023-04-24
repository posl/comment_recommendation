Synthesizing 8/10 solutions

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    g = 1
    t = 0
    while A > g**2:
        g += 1
        t += B
    t += A**0.5
    print(t)

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    if B >= 40:
        print(A ** 0.5)
        return
    if A == 1:
        print(1)
        return
    if A <= B:
        print(2)
        return
    g = 1
    t = 0
    while True:
        t += 1
        g += 1
        if t * B + ((A) / (g ** 0.5)) <= t * B + ((A) / ((g + 1) ** 0.5)):
            print(t * B + ((A) / (g ** 0.5)))
            return

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    g = 1
    t = A
    while t > g * g:
        g += 1
        t = min(t, g * g + B * (g - 1))

    print(t ** 0.5)

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    ans = 1000000000000000000
    for i in range(1000000):
        ans = min(ans, i + a / (i + 1) ** 0.5)
    print(ans)

=======
Suggestion 5

def main():
    A, B = map(int, input().split())
    ans = 0
    if A <= B:
        ans = A
    else:
        ans = B + (A - B) / (2**(1/2))
    print(ans)

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    ans = 0
    if a <= b:
        ans = a
    else:
        ans = a / ((2) ** (1 / 2))
        if ans > b:
            ans = a / ((3) ** (1 / 2))
    print(ans)

=======
Suggestion 7

def main():
    A,B = map(int,input().split())
    import math
    g = 1
    time = A/math.sqrt(g)
    while True:
        g += 1
        time = min(time, B+ A/math.sqrt(g))
        if time == B:
            break
    print(time)

=======
Suggestion 8

def main():
    A, B = map(int, input().split())
    if B >= 10**18:
        print(A)
        exit()
    if A <= B:
        print(A)
        exit()
    if A % B == 0:
        print(A/B)
        exit()
    if A < B * 2:
        print((A/B + 1))
        exit()
    print((A/B + 1 + (A%B - B) / (B+1)))
