Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    g = 1
    ans = 10**18
    for i in range(B+1):
        ans = min(ans, i + A/((g+i)**0.5))
    print(ans)

=======
Suggestion 2

def main():
    A,B = map(int,input().split())
    g = 1
    t = 0
    while True:
        if A/(g**0.5) < t:
            break
        t += B
        g += 1
    print(t)

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    g = 1
    t = 0
    while g <= A:
        g += 1
        t += B
    print(t + A / (g ** 0.5))

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    g = 1
    t = 0
    while A > t:
        t += B
        g += 1
        t += A / (g ** (1/2))
    print(t - B)

=======
Suggestion 5

def main():
    import math
    A,B = map(int,input().split())
    #A = 1000000000000000000
    #B = 100
    g = 1
    t = 0
    while True:
        t += B
        g += 1
        if A/((g)**(1/2)) <= t:
            break
    print(t)

=======
Suggestion 6

def main():
    import sys
    from math import sqrt
    input = sys.stdin.readline
    A, B = map(int, input().split())

    g = 1
    time = 0
    while True:
        if time >= A / sqrt(g):
            break
        g += 1
        time += B

    print(time - B)

=======
Suggestion 7

def main():
    A, B = map(int, input().split())
    g = 1
    ans = 0
    while True:
        if g * B + A / (g ** 0.5) < A:
            ans = g * B + A / (g ** 0.5)
            g += 1
        else:
            break
    print(ans)

=======
Suggestion 8

def main():
    A, B = map(int, input().split())

    if A <= B:
        print(A)
        return

    g = 1
    ans = float('inf')
    for i in range(100):
        ans = min(ans, i + A / (g ** 0.5))
        g += 1

    print(ans)

=======
Suggestion 9

def main():
    A,B = map(int,input().split())
    g = 1
    t = 0
    while True:
        if t + A/((g)**(1/2)) < 1 + t + B:
            print(t + A/((g)**(1/2)))
            return
        else:
            g += 1
            t += B

=======
Suggestion 10

def solve():
    A,B = map(int,input().split())
    g = 1
    ans = A/((g) ** (1/2))
    while (1):
        g += 1
        if A/((g) ** (1/2)) <= B * (g-1):
            break
        ans = A/((g) ** (1/2))
    print(ans)
    return 0
