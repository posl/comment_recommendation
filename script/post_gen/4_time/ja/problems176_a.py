Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X, T = map(int, input().split())
    if N % X == 0:
        ans = int(N / X) * T
    else:
        ans = (int(N / X) + 1) * T
    print(ans)

=======
Suggestion 2

def main():
    n, x, t = map(int, input().split())
    ans = 0
    while n > 0:
        ans += t
        n -= x
    print(ans)

=======
Suggestion 3

def main():
    N,X,T = map(int,input().split())
    if N % X == 0:
        print(int(N/X)*T)
    else:
        print((int(N/X)+1)*T)

=======
Suggestion 4

def solve():
    N,X,T = map(int,input().split())
    if N%X == 0:
        print(N//X*T)
    else:
        print((N//X+1)*T)

=======
Suggestion 5

def main():
    N,X,T = map(int, input().split())
    if N%X == 0:
        print((N//X)*T)
    else:
        print((N//X+1)*T)
main()

=======
Suggestion 6

def solve():
    n,x,t = map(int,input().split())
    a = n // x
    b = n % x
    if b != 0:
        a += 1
    print(a * t)

=======
Suggestion 7

def main():
    N,X,T = map(int,input().split())
    print((N+X-1)//X*T)

=======
Suggestion 8

def main():
    n,x,t = map(int, input().split())
    print((n+x-1)//x*t)

=======
Suggestion 9

def main():
    n,x,t = map(int,input().split())
    print(-(-n//x)*t)

=======
Suggestion 10

def main():
    N, X, T = map(int, input().split())
    print( ((N+X-1)//X)*T )
