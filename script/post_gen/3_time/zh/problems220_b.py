Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    k = int(input())
    a, b = input().split()
    a = int(a, k)
    b = int(b, k)
    print(a * b)

=======
Suggestion 3

def main():
    k = int(input())
    a, b = map(int, input().split())
    print(a*b)

=======
Suggestion 4

def main():
    k = int(input())
    a, b = map(str, input().split())
    a = int(a, k)
    b = int(b, k)
    print(a*b)

=======
Suggestion 5

def main():
    k = int(input())
    a, b = map(int, input().split())
    print(int(str(a*b), k))

=======
Suggestion 6

def main():
    # 读取数据
    k = int(input())
    a, b = input().split()
    # 从k进制转换为十进制
    a = int(a, k)
    b = int(b, k)
    # 乘法
    ans = a * b
    # 从十进制转换为k进制
    ans = str(ans)
    ans = int(ans, 10)
    print(ans)

=======
Suggestion 7

def baseKTo10(baseK, num):
    base10 = 0
    for i in range(len(num)):
        base10 += int(num[i]) * (baseK ** (len(num) - i - 1))
    return base10

=======
Suggestion 8

def toDecimal(num, base):
    num = str(num)
    result = 0
    for i in range(len(num)):
        result += int(num[-i - 1]) * (base ** i)
    return result
