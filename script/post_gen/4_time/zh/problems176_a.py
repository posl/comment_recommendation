Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def problem176_a():
    n,x,t = map(int, input().split())
    if n % x == 0:
        print(int(n/x) * t)
    else:
        print((int(n/x)+1) * t)

=======
Suggestion 2

def solve():
    n,x,t = map(int, input().split())
    print((n+x-1)//x*t)

=======
Suggestion 3

def problems176_a():
    n, x, t = map(int, input().split())
    if n % x == 0:
        print(int(n / x * t))
    else:
        print(int((n / x + 1) * t))

=======
Suggestion 4

def problem176_a():
    n,x,t = map(int, input().split())
    print((n+x-1)//x*t)

=======
Suggestion 5

def solve():
    n,x,t = map(int, input().split())
    if n % x == 0:
        print(int(n/x*t))
    else:
        print(int((n/x+1)*t))

=======
Suggestion 6

def main():
    n,x,t = map(int,input().split())
    print((n+x-1)//x*t)

=======
Suggestion 7

def problem176_a():
    n,x,t = map(int,input().split())
    return (n-1)//x*t+t

print(problem176_a())

=======
Suggestion 8

def main():
    n,x,t = map(int,input().split())
    ans = n // x * t
    if n % x != 0:
        ans += t
    print(ans)

=======
Suggestion 9

def solve():
    n,x,t = map(int,input().split())
    if n%x == 0:
        print(int(n/x)*t)
    else:
        print((int(n/x)+1)*t)
