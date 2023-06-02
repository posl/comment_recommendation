Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, a, b = map(int, input().split())
    print(n // (a + b) * a + min(n % (a + b), a))

=======
Suggestion 2

def main():
    N, A, B = map(int, input().split())
    if N == 1:
        if A == 0 and B == 0:
            print(0)
        else:
            print(1)
    else:
        if A == 0 and B == 0:
            print(0)
        else:
            print((N // (A + B)) * A + min(N % (A + B), A))

=======
Suggestion 3

def main():
    n,a,b=map(int,input().split())
    print(n//(a+b)*a+min(a,n%(a+b)))

=======
Suggestion 4

def main():
    n,a,b = map(int,input().split())
    print(a*(n//(a+b))+min(a,n%(a+b)))

=======
Suggestion 5

def main():
    n,a,b = map(int,input().split())
    c = a+b
    if n%c == 0:
        print(a*(n//c))
    else:
        if n%c <= a:
            print(a*(n//c)+n%c)
        else:
            print(a*(n//c)+a)

=======
Suggestion 6

def main():
    n, a, b = map(int, input().split())
    print((n // (a + b)) * a + min(n % (a + b), a))

=======
Suggestion 7

def main():
    n,a,b = map(int,input().split())
    if a+b == 0:
        print(0)
    else:
        print((n//(a+b))*a+min(n%(a+b),a))
