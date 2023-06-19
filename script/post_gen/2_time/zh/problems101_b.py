Synthesizing 10/10 solutions

=======
Suggestion 1

def S(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum

=======
Suggestion 2

def f(n):
    return sum(map(int, str(n)))

n = int(input())
print('Yes' if n % f(n) == 0 else 'No')

=======
Suggestion 3

def S(n):
    n_str = str(n)
    sum = 0
    for i in n_str:
        sum += int(i)
    return sum

=======
Suggestion 4

def problem101_b():
    n = int(input())
    s = sum([int(i) for i in str(n)])
    if n%s == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    N = int(input())
    S = 0
    for i in str(N):
        S += int(i)
    if N % S == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def S(n):
    result = 0
    while n > 0:
        result += n % 10
        n = n // 10
    return result

=======
Suggestion 7

def main():
    # 读取输入
    N = int(input())
    # 计算S(N)
    S = 0
    for i in str(N):
        S += int(i)
    # 判断是否能够整除
    if N % S == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def problem101_b(n):
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    if int(n) % sum == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def s(n):
    sum = 0
    while n > 0:
        sum = sum + n % 10
        n = n // 10
    return sum

n = int(input())

=======
Suggestion 10

def s(n):
    return sum([int(i) for i in str(n)])

n = int(input())
print("Yes" if n % s(n) == 0 else "No")
