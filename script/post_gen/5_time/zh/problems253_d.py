Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 2

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a%b
    return a

=======
Suggestion 3

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)

=======
Suggestion 4

def main():
    # 读取输入
    n, a, b = map(int, input().split())

    # 解决方案
    # a, b的最小公倍数
    lcm = a * b // math.gcd(a, b)

    # 1-n之间能被a或b整除的数的个数
    cnt = n // a + n // b - n // lcm

    # 1-n之间不能被a或b整除的数的个数
    cnt = n - cnt

    # 1-n之间不能被a或b整除的数的和
    ans = (1 + cnt) * cnt // 2

    # 输出
    print(ans)

=======
Suggestion 5

def main():
    # 读取输入
    n, a, b = map(int, input().split())
    # 1到n之间的整数
    num = n
    # 不是a的倍数的整数
    num -= n // a
    # 不是b的倍数的整数
    num -= n // b
    # 不是a和b的倍数的整数
    num += n // (a * b // gcd(a, b))
    # 输出结果
    print(num)

=======
Suggestion 6

def gcd(a, b):
    while(b != 0):
        t = a % b
        a = b
        b = t
    return a
