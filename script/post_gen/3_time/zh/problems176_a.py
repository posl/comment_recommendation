Synthesizing 10/10 solutions

=======
Suggestion 1

def problems176_a():
    n,x,t = map(int, input().split())
    if n%x == 0:
        print(int(n/x)*t)
    else:
        print((int(n/x)+1)*t)

=======
Suggestion 2

def time_to_make(n,x,t):
    if n%x == 0:
        return n/x*t
    else:
        return (n/x+1)*t

=======
Suggestion 3

def main():
    n, x, t = map(int, input().split())
    print(((n + x - 1) // x) * t)

=======
Suggestion 4

def problem176_a():
    n,x,t = map(int,input().split())
    if n%x != 0:
        print((n//x+1)*t)
    else:
        print((n//x)*t)

=======
Suggestion 5

def main():
    n,x,t = map(int,input().split())
    if n % x == 0:
        print(n // x * t)
    else:
        print((n // x + 1) * t)

=======
Suggestion 6

def main():
    n,x,t = map(int,input().split())
    if n%x == 0:
        print((n//x)*t)
    else:
        print((n//x+1)*t)

=======
Suggestion 7

def problem176_a():
    n,x,t = map(int,input().split())
    if n%x == 0:
        print((n//x)*t)
    else:
        print(((n//x)+1)*t)

=======
Suggestion 8

def solve():
    n, x, t = map(int, input().split())
    if n % x == 0:
        print(int(n / x) * t)
    else:
        print(int(n / x) * t + t)

=======
Suggestion 9

def make_takoyaki(n,x,t):
    if n%x == 0:
        return n//x * t
    else:
        return (n//x + 1) * t

=======
Suggestion 10

def main():
    n, x, t = map(int, input().split())
    print(int(n/x)*t)
