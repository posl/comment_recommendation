Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def floor(a,b):
    return a//b

a,b,n = map(int,input().split())

=======
Suggestion 2

def main():
    a, b, n = map(int, input().split())
    x = min(b - 1, n)
    ans = (a * x) // b - a * (x // b)
    print(ans)

=======
Suggestion 3

def main():
    a, b, n = map(int, input().split())
    x = min(n, b-1)
    print(a*x//b - a*(x//b))

=======
Suggestion 4

def main():
    a,b,n = map(int, input().split())
    x = min(n, b-1)
    print(a*x//b)

=======
Suggestion 5

def floor(a, b):
    return a // b

=======
Suggestion 6

def floor(x):
    return int(x - (x % 1))

A, B, N = map(int, input().split())

=======
Suggestion 7

def main():
    A, B, N = map(int, input().split())
    if N < B:
        print(A*N//B)
    else:
        print(A*(B-1)//B)

=======
Suggestion 8

def solve(a,b,n):
    if n<b:
        return int(a*n/b)
    else:
        return int(a*(b-1)/b)

a,b,n = map(int,input().split())
print(solve(a,b,n))

=======
Suggestion 9

def solve(a,b,n):
    if b <= n:
        x = b - 1
    else:
        x = n
    return (a*x)//b - a*(x//b)
