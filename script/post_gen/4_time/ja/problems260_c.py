Synthesizing 10/10 solutions

=======
Suggestion 1

def calc(n, x, y):
    if n == 1:
        return 1
    elif n == 2:
        return x + y
    else:
        return calc(n - 1, x, y) + calc(n - 2, x, y)

n, x, y = map(int, input().split())
print(calc(n, x, y))

=======
Suggestion 2

def calc(n, x, y):
    if n == 1:
        return 0
    if n == 2:
        return x + y
    return calc(n - 1, x, y) + calc(n - 2, x, y)

=======
Suggestion 3

def solve():
    #n, x, y = map(int, input().split())
    n, x, y = 10, 5, 5
    #n, x, y = 2, 3, 4

    #dp = [0] * (n + 1)
    #dp[1] = 1
    #for i in range(2, n + 1):
    #    dp[i] = min(dp[i - 1] + x, dp[i // 2] + y) if i % 2 == 0 else dp[i - 1] + x
    #print(dp[n])

    #dp = [0] * (n + 1)
    #dp[1] = 1
    #for i in range(2, n + 1):
    #    dp[i] = dp[i - 1] + x
    #    if i % 2 == 0:
    #        dp[i] = min(dp[i], dp[i // 2] + y)
    #print(dp[n])

    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(1, n):
        dp[i + 1] = min(dp[i + 1], dp[i] + x)
        if i * 2 <= n:
            dp[i * 2] = min(dp[i * 2], dp[i] + y)
    print(dp[n])

=======
Suggestion 4

def get_blue_gem_count(n, x, y):
    if n == 1:
        return 0
    elif n == 2:
        return x
    else:
        return get_blue_gem_count(n-1, x, y) + get_blue_gem_count(n-2, x, y) + y

=======
Suggestion 5

def solve():
    n,x,y = map(int,input().split())
    if x >= y:
        print((n-1)*y)
    else:
        print((n-1)*x)

=======
Suggestion 6

def getStoneNum(n, x, y):
    if n == 1:
        return 0
    if n == 2:
        return x + y
    return getStoneNum(n-1, x, y) + getStoneNum(n-2, x, y)

n, x, y = map(int, input().split())
print(getStoneNum(n, x, y))

=======
Suggestion 7

def rec(n):
    if n==1:
        return 0
    if n in dp:
        return dp[n]
    dp[n]=rec(n-1)+X
    if n%2==0:
        dp[n]=min(dp[n],rec(n//2)+Y)
    else:
        dp[n]=min(dp[n],rec(n//2+1)+Y+X)
        dp[n]=min(dp[n],rec(n//2)+Y+X)
    return dp[n]

N,X,Y=map(int,input().split())
dp={}
print(rec(N))

=======
Suggestion 8

def calc_blue_gem(level, red, blue, x, y):
    if level == 1:
        return blue
    elif level == 2:
        return blue + red * x
    else:
        return calc_blue_gem(level-1, red, blue, x, y) * y + calc_blue_gem(level-2, red, blue, x, y) * x

=======
Suggestion 9

def solve():
    N,X,Y = map(int,input().split())
    print((N-1)*min(X,Y)+1)

=======
Suggestion 10

def solve():
    N,X,Y = map(int,input().split())
    print(N,X,Y)
    print('N:',N)
    print('X:',X)
    print('Y:',Y)
    print('solve()')
