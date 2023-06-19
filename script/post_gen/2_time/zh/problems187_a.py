Synthesizing 10/10 solutions

=======
Suggestion 1

def get_sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

=======
Suggestion 2

def s(n):
    n = str(n)
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    return sum

a, b = map(int, input().split())
print(s(a) if s(a) > s(b) else s(b))

=======
Suggestion 3

def s(n):
    sum = 0
    for i in range(3):
        sum += n % 10
        n //= 10
    return sum

a, b = map(int, input().split())
print(s(a) if s(a) > s(b) else s(b))

=======
Suggestion 4

def sumOfDigits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

=======
Suggestion 5

def main():
    # 获取输入
    input_line = input()
    # 分割输入
    input_line = input_line.split()
    # 获取第一个数字
    first_num = input_line[0]
    # 获取第二个数字
    second_num = input_line[1]
    # 计算第一个数字的总和
    first_num_sum = 0
    for i in range(len(first_num)):
        first_num_sum += int(first_num[i])
    # 计算第二个数字的总和
    second_num_sum = 0
    for i in range(len(second_num)):
        second_num_sum += int(second_num[i])
    # 输出
    if first_num_sum > second_num_sum:
        print(first_num_sum)
    elif first_num_sum < second_num_sum:
        print(second_num_sum)
    else:
        print(first_num_sum)

=======
Suggestion 6

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

A, B = map(int, input().split())
print(max(sum_digits(A), sum_digits(B)))

=======
Suggestion 7

def sum_of_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num = num // 10
    return sum

=======
Suggestion 8

def main():
    num1, num2 = map(int, input().split())
    sum1 = sum([int(i) for i in str(num1)])
    sum2 = sum([int(i) for i in str(num2)])
    if sum1 >= sum2:
        print(sum1)
    else:
        print(sum2)

=======
Suggestion 9

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

a, b = map(int, input().split())
print(max(sum_digits(a), sum_digits(b)))

=======
Suggestion 10

def main():
    a, b = map(int, input().split())
    print(max(sum([int(x) for x in str(a)]), sum([int(x) for x in str(b)])))
