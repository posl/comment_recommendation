Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, A, B = map(int, input().split())
    if A > B:
        print(0)
    elif N == 1:
        if A == B:
            print(1)
        else:
            print(0)
    else:
        print((N - 2) * B + A - (N - 2) * A - B + 1)

=======
Suggestion 2

def getBlueCount(n, a, b):
    if a == 0:
        return 0
    if b == 0:
        return n
    if a + b >= n:
        return a
    else:
        return a + (n - a - b)

=======
Suggestion 3

def problems158_b():
    n,a,b = map(int,input().split())
    if a == 0:
        print(0)
        return
    if a+b >= n:
        print(a)
        return
    else:
        print(a+(n-a-b))

=======
Suggestion 4

def main():
    n,a,b = map(int,input().split())
    print(n//(a+b)*a+min(a,n%(a+b)))

=======
Suggestion 5

def main():
    # 读取输入
    n, a, b = map(int, input().split())
    # 蓝球数
    blue = 0
    # 蓝球数增加的次数
    count = 0
    # 蓝球数增加的次数限制
    limit = 10 ** 100
    while count < limit:
        # 增加蓝球数
        blue = blue + a
        # 增加蓝球数增加的次数
        count = count + 1
        # 如果增加蓝球数的次数达到限制，跳出循环
        if count == limit:
            break
        # 增加红球数
        blue = blue - b
        # 增加蓝球数增加的次数
        count = count + 1
        # 如果增加蓝球数的次数达到限制，跳出循环
        if count == limit:
            break
    # 打印蓝球数
    print(blue)

=======
Suggestion 6

def main():
    N,A,B = map(int,input().split())
    if A == 0:
        print(0)
    elif A + B == 1:
        print(N)
    else:
        print(N//(A+B)*A+min(N%(A+B),A))

=======
Suggestion 7

def main():
    N, A, B = map(int, input().split())
    if A == 0:
        print(0)
    elif B == 0:
        print(N)
    else:
        print(N // (A + B) * A + min(N % (A + B), A))

=======
Suggestion 8

def main():
    n, a, b = map(int, input().split())
    print((n // (a + b)) * a + min(n % (a + b), a))

=======
Suggestion 9

def blue_ball(n, a, b):
    if n == 1:
        return a
    elif n == 2:
        return a+b
    else:
        return blue_ball(n-1, a, b) + blue_ball(n-2, a, b)

=======
Suggestion 10

def main():
    # 读取输入
    n, a, b = map(int, input().split())
    # 用a+b表示蓝球和红球的总数
    if a + b == 0:
        print(0)
    elif n == 1:
        print(a)
    else:
        # 当n>1时，可以将n-1个球放在一行
        # 一行中有a+b-1个球，其中a-1个球是蓝色的
        # 因此，一行中有a-1个蓝球
        # 一行中有b个红球
        # 一行中有a+b-1个球
        # 一行中有a-1个蓝球
        # 一行中有b个红球
        # 一行中有a+b-1个球
        # 一行中有a-1个蓝球
        # 一行中有b个红球
        # 一行中有a+b-1个球
        # 一行中有a-1个蓝球
        # 一行中有b个红球
        # 一行中有a+b-1个球
        # 一行中有a-1个蓝球
        # 一行中有b个红球
        # 一行中有a+b-1个球
        # 一行中有a-1个蓝球
        # 一行中有b个红球
        # 一行中有a+b-1个球
        # 一行中有a-1个蓝球
        # 一行中有b个红球
        # 一行中有a+b-1个球
        # 一行中有a-1个蓝球
        # 一行中有b个红球
        # 一行中有a+b-1个球
        # 一行中有a-1个蓝球
        # 一行中有b个红球
        # 一行中有
