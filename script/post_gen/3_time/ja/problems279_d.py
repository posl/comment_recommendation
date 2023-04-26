Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    import sys
    import math
    input = sys.stdin.readline
    a, b = map(int, input().split())
    print(math.sqrt(a)*b)

=======
Suggestion 2

def main():
    a,b = map(int,input().split())
    print(((a)/((1)^(1/2)))+((b)/((2)^(1/2))))

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    print((A + B - 1) / B)

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    print((a/b)**(1/2))

=======
Suggestion 5

def solve():
    A, B = map(int, input().split())
    g = 1
    time = A
    while True:
        if time <= B:
            break
        g += 1
        time = (A + time) / 2
    print(time)

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def solve():
    A, B = map(int, input().split())
    if A >= B:
        print(A)
    else:
        print((B-1)/2)

=======
Suggestion 8

def solve():
    import sys
    import math
    input = sys.stdin.readline
    a, b = map(int, input().split())
    c = 0
    while True:
        if a * c >= b:
            break
        c += 1
    g = 1
    ans = 0
    while True:
        ans += a / math.sqrt(g)
        if g == c + 1:
            break
        g += 1
    print(ans)

=======
Suggestion 9

def solve():
    A, B = list(map(int, input().split()))
    if A >= B:
        print(A)
    else:
        print((2*A+B)/(2**0.5))

=======
Suggestion 10

def my_ceil(a, b):
    return -(-a // b)

a, b = map(int, input().split())
