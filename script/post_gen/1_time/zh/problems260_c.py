Synthesizing 10/10 solutions

=======
Suggestion 1

def getBlueNum(n, x, y):
    if n == 1:
        return 0
    if n == 2:
        return x
    if n == 3:
        return x + y
    if n > 3:
        return getBlueNum(n-1, x, y) + getBlueNum(n-2, x, y)

=======
Suggestion 2

def getBlueStoneCount(redStoneCount, x, y):
    if redStoneCount == 1:
        return 0
    if redStoneCount == 2:
        return x
    else:
        return getBlueStoneCount(redStoneCount - 1, x, y) + getBlueStoneCount(redStoneCount - 2, x, y) + y

=======
Suggestion 3

def f(n,x,y):
    if n==1:
        return 0
    else:
        return 1+f(n-1,x,y)+f(n-1,x,y)

=======
Suggestion 4

def main():
    n,x,y = map(int,input().split())
    ans = 0
    for i in range(1,n):
        if i <= x:
            ans += (n-i)*x+1-i
        else:
            ans += y*(n-i)+1-i
    print(ans)

=======
Suggestion 5

def calc(n,x,y):
    if n == 1:
        return 0
    elif n == 2:
        return x
    else:
        return calc(n-1,x,y) + calc(n-2,x,y) + y

n,x,y = map(int,input().split())
print(calc(n,x,y))

=======
Suggestion 6

def calc(n, x, y):
    if n == 1:
        return 0
    if n == 2:
        return x

    # 1级红宝石
    r1 = 1

    # 2级红宝石
    r2 = 0

    # 1级蓝宝石
    b1 = 0

    # 2级蓝宝石
    b2 = 0

    for i in range(2, n + 1):
        b2 = b1
        b1 = r2 * y
        r2 = r1
        r1 = b2 + x

    return b1

=======
Suggestion 7

def main():
    n,x,y = map(int,input().split())
    print(n,x,y)
    ans = 0
    for i in range(1,n):
        ans += max(0, n-i-1) * x
        print(ans)
    for i in range(1,n):
        ans += max(0, n-i-1) * y
        print(ans)
    print(ans)

=======
Suggestion 8

def gem(N,X,Y):
    if X > Y:
        return 0
    elif X == Y:
        if N % 2 == 0:
            return (N // 2) * X
        else:
            return (N // 2) * X + 1
    else:
        if N % 2 == 0:
            return (N // 2) * (X + Y)
        else:
            return (N // 2) * (X + Y) + X

=======
Suggestion 9

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
Suggestion 10

def main():
    pass
