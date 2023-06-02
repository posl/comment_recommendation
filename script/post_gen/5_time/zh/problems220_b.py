Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    k = int(input())
    a,b = map(int,input().split())
    print(a*b)

=======
Suggestion 2

def baseK_to_base10(s,k):
    s = s[::-1]
    result = 0
    for i in range(len(s)):
        result += int(s[i])*(k**i)
    return result
k = int(input())
a,b = map(str,input().split())
a = baseK_to_base10(a,k)
b = baseK_to_base10(b,k)
print(a*b)

=======
Suggestion 3

def base_k_to_10(num, k):
    result = 0
    for i in range(len(num)):
        result += int(num[i]) * k**(len(num)-i-1)
    return result

=======
Suggestion 4

def main():
    k = int(input())
    a,b = input().split()
    a = int(a,k)
    b = int(b,k)
    print(a*b)

=======
Suggestion 5

def main():
    # 读入数据
    K = int(input())
    A, B = map(int, input().split())
    # 将A，B转换为10进制
    A = int(str(A), K)
    B = int(str(B), K)
    # 计算并打印结果
    print(A*B)

=======
Suggestion 6

def main():
    k = int(input())
    a, b = map(int, input().split())
    print(int(str(a * b), k))

=======
Suggestion 7

def convert_to_decimal(num, base):
    multiplier, result = 1, 0
    while num > 0:
        result += num % 10 * multiplier
        multiplier *= base
        num //= 10
    return result

=======
Suggestion 8

def f(k, a, b):
    a_10 = 0
    b_10 = 0
    for i in range(len(a)):
        a_10 += int(a[i]) * pow(k, len(a) - i - 1)
    for i in range(len(b)):
        b_10 += int(b[i]) * pow(k, len(b) - i - 1)
    return a_10 * b_10

k = int(input())
a, b = input().split()
print(f(k, a, b))
