Synthesizing 10/10 solutions

=======
Suggestion 1

def calc_price(a, b, n):
    return a * n + b * len(str(n))

a, b, x = map(int, input().split())

=======
Suggestion 2

def get_digit(n):
    digit = 0
    while n > 0:
        n = n // 10
        digit += 1
    return digit

=======
Suggestion 3

def main():
    # A, B, X = map(int, input().split())
    # N = (X - B) // A
    # print(N if N <= 10**9 else 10**9)

    # 二分探索で解く
    A, B, X = map(int, input().split())
    l = 0
    r = 10**9 + 1
    while r - l > 1:
        m = (l + r) // 2
        if A * m + B * len(str(m)) <= X:
            l = m
        else:
            r = m
    print(l)

=======
Suggestion 4

def main():
    # input
    A, B, X = map(int, input().split())

    # compute
    N = 0
    for i in range(1, 10):
        if X >= A*i + B*(len(str(i))):
            N = i
        else:
            break

    # output
    print(N)

=======
Suggestion 5

def main():
    a, b, x = map(int, input().split())
    l = 0
    r = 1000000001
    while(r - l > 1):
        m = (l + r) // 2
        if(a * m + b * len(str(m)) > x):
            r = m
        else:
            l = m
    print(l)

=======
Suggestion 6

def main():
    A, B, X = map(int, input().split())
    def f(N):
        return A * N + B * len(str(N))
    l = 0
    r = 10 ** 9 + 1
    while r - l > 1:
        m = (l + r) // 2
        if f(m) <= X:
            l = m
        else:
            r = m
    print(l)

=======
Suggestion 7

def func(a,b,x):
    if a+b > x:
        return 0
    if a*10+b*10 <= x:
        return 10**9
    if a*9+b*9 <= x:
        return 10**8
    if a*8+b*8 <= x:
        return 10**7
    if a*7+b*7 <= x:
        return 10**6
    if a*6+b*6 <= x:
        return 10**5
    if a*5+b*5 <= x:
        return 10**4
    if a*4+b*4 <= x:
        return 10**3
    if a*3+b*3 <= x:
        return 10**2
    if a*2+b*2 <= x:
        return 10**1
    if a+b <= x:
        return 10**0
    return 0

=======
Suggestion 8

def main():
    a,b,x = map(int,input().split())
    max = 0
    for i in range(1,10):
        if x >= a * i + b * len(str(i)):
            max = i
    print(max)

=======
Suggestion 9

def main():
    a,b,x = map(int,input().split())
    if a*10 + b*1 > x:
        print(0)
        return
    # 二分探索
    # 1以上10^9以下の整数
    ok = 10**9
    ng = 0
    while abs(ok-ng) > 1:
        mid = (ok+ng)//2
        if a*mid + b*len(str(mid)) <= x:
            ng = mid
        else:
            ok = mid
    print(ng)

=======
Suggestion 10

def main():
    a,b,x = map(int,input().split())
    if a * 10 + b * 1 > x:
        print(0)
        exit()
    elif a * 10 ** 9 + b * 10 > x:
        print(10 ** 9)
        exit()
    else:
        for i in range(10,0,-1):
            if a * i * 10 ** (i - 1) + b * i <= x:
                print(i * 10 ** (i - 1))
                exit()
