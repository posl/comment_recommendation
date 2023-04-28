Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, N = map(int, input().split())
    x = min(B-1, N)
    print((A*x)//B - A*(x//B))

=======
Suggestion 2

def main():
    a, b, n = map(int, input().split())
    if b-1 <= n:
        x = b-1
    else:
        x = n
    print((a*x)//b - a*(x//b))

=======
Suggestion 3

def main():
    A, B, N = map(int, input().split())
    if N < B:
        print(A*N//B)
    else:
        print(A*(B-1)//B)

=======
Suggestion 4

def main():
    A,B,N = map(int,input().split())
    if N < B:
        x = N
    else:
        x = B - 1
    print((A*x)//B - A*(x//B))

=======
Suggestion 5

def main():
    a,b,n = map(int,input().split())
    x = min(b-1,n)
    print((a*x)//b)

=======
Suggestion 6

def main():
    a, b, n = map(int, input().split())
    x = min(n, b-1)
    print(int(a*x/b)-a*int(x/b))

=======
Suggestion 7

def main():
    a,b,n = map(int,input().split())
    x = min(n,b-1)
    print(int((a*x)/b) - a*int(x/b))

=======
Suggestion 8

def main():
    a,b,n = map(int,input().split())
    x = min(b-1,n)
    print(int(a*x/b)-a*int(x/b))

main()

=======
Suggestion 9

def floor(a,b):
    return int(a/b)

A,B,N = map(int,input().split())

x = min(B-1,N)

print(floor(A*x/B)-A*floor(x/B))

=======
Suggestion 10

def floor(a, b):
    return a // b
