Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    i = 1
    while i * i <= N:
        if N % i == 0:
            print(i)
            if i * i != N:
                print(N // i)
        i += 1

=======
Suggestion 2

def main():
    N = int(input())
    i = 1
    while i * i <= N:
        if N % i == 0:
            print(i)
            if i != N // i:
                print(N // i)
        i += 1

=======
Suggestion 3

def main():
    n = int(input())
    result = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            result.append(i)
            if i != n // i:
                result.append(n // i)
    result.sort()
    for i in result:
        print(i)

=======
Suggestion 4

def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

n = int(input())
divisors = get_divisors(n)
print(*sorted(divisors), sep='\n')

=======
Suggestion 5

def get_divisor(n):
    """求一个数的约数"""
    if n == 1:
        return [1]
    else:
        i = 1
        divisor = []
        while i*i <= n:
            if n % i == 0:
                divisor.append(i)
                if i*i != n:
                    divisor.append(n//i)
            i += 1
        divisor.sort()
        return divisor

n = int(input())
divisor = get_divisor(n)
for i in divisor:
    print(i)

=======
Suggestion 6

def main():
    # 读取输入
    N = int(input())
    # 初始化结果列表
    result = []
    # 遍历
    for i in range(1, int(N ** 0.5) + 1):
        # 如果可以整除
        if N % i == 0:
            # 加入结果
            result.append(i)
            # 如果不是平方数
            if N // i != i:
                # 加入结果
                result.append(N // i)
    # 排序
    result.sort()
    # 输出结果
    for i in result:
        print(i)

=======
Suggestion 7

def main():
    N = int(input())
    i = 1
    while i ** 2 <= N:
        if N % i == 0:
            print(i)
            if i != N // i:
                print(N // i)
        i += 1

=======
Suggestion 8

def main():
    N = int(input())
    ans = []
    i = 1
    while i * i <= N:
        if N % i == 0:
            ans.append(i)
            if i * i != N:
                ans.append(N // i)
        i += 1
    ans.sort()
    for i in ans:
        print(i)

=======
Suggestion 9

def main():
    n = int(input())
    i = 1
    while i * i <= n:
        if n % i == 0:
            print(i)
            if i * i != n:
                print(n // i)
        i += 1
