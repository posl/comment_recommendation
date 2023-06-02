Synthesizing 10/10 solutions

=======
Suggestion 1

def f(n, x, y):
    if x > y:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return x
    return f(n-1, x, y) + (n-1) * f(n-2, x, y)

n, x, y = map(int, input().split())
print(f(n, x, y))

=======
Suggestion 2

def make_blue(n,x,y):
    if n == 1:
        return 1
    elif n == 2:
        return 0
    else:
        return make_blue(n-1,x,y) + make_red(n-1,x,y) * y

=======
Suggestion 3

def f(n, x, y):
    if n == 1:
        return 1
    if n == 2:
        return 0
    return f(n-1, x, y) + f(n-2, x, y) + x * f(n-1, x, y) + y * f(n-2, x, y)

=======
Suggestion 4

def getBlueNum(n, x, y):
    if n == 1:
        return 0
    if n == 2:
        return x
    if n == 3:
        return x + y
    return getBlueNum(n-1, x, y) + getBlueNum(n-2, x, y)

=======
Suggestion 5

def getN1(n,x,y):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return getN1(n-1,x,y) + x * getN2(n-1,x,y)

=======
Suggestion 6

def problems260_c():
    pass

=======
Suggestion 7

def main():
    n, x, y = map(int, input().split())
    #print(n, x, y)
    #print(type(n), type(x), type(y))

    #宝石的最大数量
    MAX = 10
    #dp[i]表示i个宝石的最大数量
    dp = [0] * (MAX + 1)
    dp[2] = 1

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + x
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + y)

    print(dp[n])

=======
Suggestion 8

def f(n,x,y):
    if n == 1:
        return 0
    if n == 2:
        return x
    if n == 3:
        return x + y
    return f(n-1,x,y) + f(n-2,x,y) + f(n-3,x,y)

=======
Suggestion 9

def main():
    pass

=======
Suggestion 10

def main():
    n,x,y = map(int, input().split())
    ans = 0
    for i in range(1,n):
        ans += max(0, n-i-1) * x
    print(ans)
