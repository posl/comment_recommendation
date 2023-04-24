Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, x, t = map(int, input().split())
    if n % x == 0:
        print((n // x) * t)
    else:
        print(((n // x) + 1) * t)

=======
Suggestion 2

def main():
    N, X, T = map(int, input().split())
    if N % X == 0:
        print(int(N / X) * T)
    else:
        print((int(N / X) + 1) * T)

=======
Suggestion 3

def main():
    n, x, t = map(int, input().split())
    if n % x == 0:
        print(int(n / x) * t)
    else:
        print((int(n / x) + 1) * t)

=======
Suggestion 4

def solve():
    n, x, t = map(int, input().split())
    if n % x == 0:
        print((n//x) * t)
    else:
        print(((n//x)+1) * t)

=======
Suggestion 5

def solve():
    N, X, T = map(int, input().split())
    print(((N - 1) // X + 1) * T)

=======
Suggestion 6

def main():
    N,X,T = map(int,input().split())
    if N % X == 0:
        print(int(N/X * T))
    else:
        print(int((N//X + 1) * T))

=======
Suggestion 7

def main():
    n,x,t = map(int,input().split())
    if n % x == 0:
        print(int((n/x)*t))
    else:
        print(int(((n//x)+1)*t))

main()

=======
Suggestion 8

def main():
    n,x,t = map(int,input().split())
    time = 0
    while n > 0:
        n -= x
        time += t
    print(time)
