Synthesizing 10/10 solutions

=======
Suggestion 1

def calc(n, x, y):
    if n == 1:
        return 1
    elif n == 2:
        return x + y
    else:
        return calc(n-1, x, y) + calc(n-2, x, y)

=======
Suggestion 2

def calc(n, x, y):
    if n == 1:
        return 0
    elif n == 2:
        return x + y
    else:
        return calc(n-1, x, y) + calc(n-2, x, y) + x

n, x, y = map(int, input().split())
print(calc(n, x, y))

=======
Suggestion 3

def func(n, x, y):
    if n == 1:
        return 0
    if n == 2:
        return x + y
    return func(n-1, x, y) + func(n-2, x, y)

n, x, y = map(int, input().split())
print(func(n, x, y))

=======
Suggestion 4

def solve():
    N, X, Y = map(int, input().split())
    dp = [0]*(N+1)
    dp[1] = 1
    for i in range(2, N+1):
        dp[i] = dp[i-1] + X
        for j in range(2, i):
            dp[i] = min(dp[i], dp[j-1] + X + (i-j)*Y)
    print(dp[-1])
    return 0

=======
Suggestion 5

def calc(n, x, y):
    if n == 1:
        return 0
    if n == 2:
        return x
    if n == 3:
        return x + y
    return calc(n - 1, x, y) + calc(n - 2, x, y)

n, x, y = map(int, input().split())
print(calc(n, x, y))

=======
Suggestion 6

def calc(N, X, Y):
    if N == 1:
        return 0
    if N == 2:
        return X + Y
    return calc(N-1, X, Y) + calc(N-2, X, Y)

=======
Suggestion 7

def calc(x, y, n):
    if n == 1:
        return 0
    elif n == 2:
        return x + y
    else:
        return calc(x, y, n-1) + calc(x, y, n-2)

n, x, y = map(int, input().split())
print(calc(x, y, n))

=======
Suggestion 8

def func(n,x,y):
    if n==1:
        return 0
    elif n==2:
        return x+y
    else:
        return func(n-1,x,y)*2+x+y

n,x,y=map(int,input().split())
print(func(n,x,y))

=======
Suggestion 9

def calc(n, x, y):
    if n == 1:
        return 0
    elif n == 2:
        return x
    else:
        return x + y + calc(n-1, x, y)

=======
Suggestion 10

def calc(n,x,y):
    if n==1:
        return 1
    elif n==2:
        return x+1
    elif n==3:
        return x+1+x*y+1
    else:
        return x+calc(n-1,x,y)+calc(n-2,x,y)
n,x,y=map(int,input().split())
print(calc(n,x,y))
