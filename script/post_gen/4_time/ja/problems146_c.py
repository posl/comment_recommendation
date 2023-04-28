Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, x = map(int, input().split())
    if a > x:
        print(0)
        return
    if a * 1000000000 + b * 10 <= x:
        print(1000000000)
        return
    left = 0
    right = 1000000000
    while left + 1 < right:
        mid = (left + right) // 2
        if a * mid + b * len(str(mid)) <= x:
            left = mid
        else:
            right = mid
    print(left)

=======
Suggestion 2

def get_digit(x):
    digit = 0
    while x > 0:
        x //= 10
        digit += 1
    return digit

=======
Suggestion 3

def main():
    a,b,x = map(int, input().split())
    ans = 0
    if a * 10 + b * 1 <= x:
        ans = 10
    elif a * 1 + b * 1 <= x:
        ans = 1
    else:
        ans = 0
    print(ans)

=======
Suggestion 4

def main():
    A,B,X = map(int,input().split())
    ans = 0
    for i in range(1,11):
        if A*i + B*len(str(i)) <= X:
            ans = i
    print(ans)

=======
Suggestion 5

def main():
    a, b, x = map(int, input().split())
    result = 0
    for d in range(1, 10):
        n = (x - b * d) // a
        if n > 0 and len(str(n)) == d:
            result = n if result < n else result
    print(result)

=======
Suggestion 6

def main():
    a, b, x = map(int, input().split())
    ans = 0
    for i in range(1, 10):
        if x < a * 10 ** i + b * i:
            ans = i - 1
            break
    if x >= a * 10 ** 9 + b * 10:
        ans = 10 ** 9
    print(ans)

=======
Suggestion 7

def main():
    A,B,X = map(int, input().split())
    ans = 0
    for i in range(1,10):
        if A*i+B*len(str(i)) > X:
            break
        ans = i
    print(ans)

=======
Suggestion 8

def main():
    a, b, x = [int(i) for i in input().split()]
    n = 0
    for i in range(1,10):
        if x >= a * (10 ** i) + b * i:
            n = 10 ** i
    if n == 0:
        print(0)
    else:
        print(min((x - b * len(str(n))) // a, n - 1))

=======
Suggestion 9

def main():
    a, b, x = map(int, input().split())
    #print(a, b, x)
    #print(len(str(x)))
    #print(x // (a+b))
    if a + b > x:
        print(0)
    else:
        if a * (10 ** 9) + b * 10 < x:
            print(10 ** 9)
        else:
            print((x - b) // a)
    return

=======
Suggestion 10

def main():
    A,B,X = map(int,input().split())
    # 最大の整数を買うことができるかどうかを判定する関数
    def is_ok(n):
        if A * n + B * len(str(n)) <= X:
            return True
        else:
            return False

    # 二分探索
    def meguru_bisect(ng, ok):
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    # ng = 0
    # ok = 10**9+1
    print(meguru_bisect(0, 10**9+1))
