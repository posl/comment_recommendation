Synthesizing 10/10 solutions

=======
Suggestion 1

def func(n, x, y):
    if n == 1:
        return 0
    if n == 2:
        return x
    else:
        return func(n-1, x, y) + func(n-2, x, y) + y

=======
Suggestion 2

def calcBlue(n, x, y):
    if n == 1:
        return 1
    if n == 2:
        return x
    return calcBlue(n-1, x, y) + calcBlue(n-2, x, y)*y

=======
Suggestion 3

def f(n, x, y):
    if n == 1:
        return 1
    elif n == 2:
        return x
    else:
        return f(n-1, x, y) + f(n-2, x, y) + y

=======
Suggestion 4

def main():
    n,x,y = map(int,input().split())
    if x > y:
        print(0)
    else:
        print((n-1)*x)

=======
Suggestion 5

def main():
    N, X, Y = map(int, input().split())
    result = 0
    for i in range(N-1, 0, -1):
        if i >= X:
            result += 1
        else:
            result += 1 + (X - i) * (N - i - 1)
    print(result)

=======
Suggestion 6

def solve(N,X,Y):
    if N == 1:
        return 0
    elif N == 2:
        return 1
    else:
        return solve(N-1,X,Y) + solve(N-2,X,Y) + X

=======
Suggestion 7

def solve(n,x,y):
    if n==1:
        return 0
    else:
        return (n-1)*min(x,y)+solve(n-1,x,y)

=======
Suggestion 8

def f(n,x,y):
    if n==1:
        return 0
    elif n==2:
        return x
    else:
        return f(n-1,x,y)+f(n-2,x,y)+y

n,x,y=map(int,input().split())
print(f(n,x,y))

=======
Suggestion 9

def get_num(n,x,y):
    if n == 1:
        return 0
    if n == 2:
        return x + y
    else:
        return get_num(n-1,x,y) + get_num(n-2,x,y) + x

N,X,Y = map(int,input().split())
print(get_num(N,X,Y))

=======
Suggestion 10

def main():
    pass
