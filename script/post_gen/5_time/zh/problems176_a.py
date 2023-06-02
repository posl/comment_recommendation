Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def problems176_a():
    N,X,T = map(int, input().split())
    if N%X==0:
        print(int(N/X)*T)
    else:
        print((int(N/X)+1)*T)

=======
Suggestion 2

def problems176_a():
    n,x,t = map(int,input().split())
    if n%x == 0:
        print(int(n/x)*t)
    else:
        print((int(n/x)+1)*t)

=======
Suggestion 3

def main():
    n,x,t = map(int,input().split())
    if n%x == 0:
        print((n//x)*t)
    else:
        print((n//x+1)*t)

=======
Suggestion 4

def problems176_a():
    N, X, T = map(int, input().split())
    print((N+X-1)//X*T)

=======
Suggestion 5

def main():
    n,x,t = map(int,input().split())
    if n%x == 0:
        print(n//x*t)
    else:
        print((n//x+1)*t)

=======
Suggestion 6

def main():
    n, x, t = map(int, input().split())
    print((n + x - 1) // x * t)

=======
Suggestion 7

def problem176_a():
    n,x,t = map(int,input().split())
    print(((n-1)//x+1)*t)

=======
Suggestion 8

def problem176_a():
    n, x, t = map(int, input().split())
    if n % x == 0:
        print(int(n / x) * t)
    else:
        print((int(n / x) + 1) * t)

=======
Suggestion 9

def calc_time():
    n,x,t = input("请输入N,X,T\n").split(" ")
    n = int(n)
    x = int(x)
    t = int(t)
    if n%x == 0:
        return (n//x)*t
    else:
        return (n//x)*t+t
