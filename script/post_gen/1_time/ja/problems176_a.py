Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, x, t = map(int, input().split())
    if n % x == 0:
        print(n // x * t)
    else:
        print((n // x + 1) * t)

=======
Suggestion 2

def solve():
    N,X,T = map(int, input().split())
    if N % X == 0:
        print((N // X) * T)
    else:
        print(((N // X) + 1) * T)

=======
Suggestion 3

def main():
    n,x,t = map(int,input().split())
    if n%x == 0:
        print(t*(n//x))
    else:
        print(t*(n//x+1))

=======
Suggestion 4

def solve():
    N,X,T = map(int, input().split())
    if N%X == 0:
        print(N//X*T)
    else:
        print((N//X+1)*T)

=======
Suggestion 5

def main():
    n,x,t = map(int,input().split())
    if n % x == 0:
        print(int(n/x*t))
    else:
        print(int((n/x+1)*t))

=======
Suggestion 6

def solve():
    N, X, T = map(int, input().split())
    print((N+X-1)//X*T)

=======
Suggestion 7

def main():
    N,X,T = map(int,input().split())
    print((N+X-1)//X*T)

=======
Suggestion 8

def main():
    N, X, T = map(int, input().split())
    print((N+X-1)//X*T)
main()

=======
Suggestion 9

def solve():
    n,x,t = map(int, input().split())
    print(-(-n//x)*t)
