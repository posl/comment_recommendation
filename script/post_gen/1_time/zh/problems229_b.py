Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if a + b >= 10**10:
        print("Hard")
    else:
        print("Easy")

=======
Suggestion 2

def plus(a, b):
    if a == 0 and b == 0:
        return 0
    elif a == 0:
        return b
    elif b == 0:
        return a

    result = 0
    carry = 0
    while a > 0 and b > 0:
        if a % 10 + b % 10 + carry >= 10:
            carry = 1
        else:
            carry = 0
        a = a // 10
        b = b // 10
        result = result * 10 + carry
    while a > 0:
        if a % 10 + carry >= 10:
            carry = 1
        else:
            carry = 0
        a = a // 10
        result = result * 10 + carry
    while b > 0:
        if b % 10 + carry >= 10:
            carry = 1
        else:
            carry = 0
        b = b // 10
        result = result * 10 + carry
    return result

=======
Suggestion 3

def solve():
    a,b = map(int,input().split())
    if a+b>=10**18:
        print("Hard")
    else:
        print("Easy")

=======
Suggestion 4

def main():
    #读取输入
    inputs = input().split()
    #将读取的输入转换为整数
    A = int(inputs[0])
    B = int(inputs[1])
    #计算A+B
    sum = A + B
    #如果sum小于10^18，输出Easy
    if sum < 10**18:
        print("Easy")
    #如果sum大于等于10^18，输出Hard
    else:
        print("Hard")

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    if a + b < 10:
        print("Easy")
    else:
        print("Hard")

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    if a + b >= 10 ** 10:
        print('Hard')
    else:
        print('Easy')

=======
Suggestion 7

def add(a, b):
    return a + b

=======
Suggestion 8

def main():
    a, b = map(int, input().split())
    if a + b < 10:
        print('Easy')
    else:
        print('Hard')
