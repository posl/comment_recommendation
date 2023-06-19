Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def problems176_a():
    n,x,t = map(int, input().split())
    print((n+x-1)//x * t)

=======
Suggestion 2

def main():
    n,x,t = map(int, input().split())
    print((n + x - 1) // x * t)

=======
Suggestion 3

def main():
    n,x,t = map(int,input().split())
    print(t*((n+x-1)//x))

=======
Suggestion 4

def solve():
    n,x,t = map(int, input().split())
    if n % x == 0:
        print(n // x * t)
    else:
        print((n // x + 1) * t)

=======
Suggestion 5

def problem176_a():
    n, x, t = map(int, input().split())
    if n % x == 0:
        print((n // x) * t)
    else:
        print((n // x + 1) * t)

problem176_a()

=======
Suggestion 6

def main():
    n,x,t = map(int,input().split())
    print((n//x + (n%x>0))*t)

=======
Suggestion 7

def prob_176_a(n, x, t):
    if n % x == 0:
        return n // x * t
    else:
        return (n // x + 1) * t

=======
Suggestion 8

def problem176_a():
    n, x, t = map(int, input().split())
    print((n + x - 1) // x * t)

=======
Suggestion 9

def main():
    n, x, t = map(int, input().split())
    if n % x == 0:
        print((n // x) * t)
    else:
        print(((n // x) + 1) * t)
