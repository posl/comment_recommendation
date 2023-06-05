Synthesizing 10/10 solutions

=======
Suggestion 1

def problem200_b(n, k):
    for i in range(k):
        if n % 200 == 0:
            n = n // 200
        else:
            n = int(str(n) + '200')
    return n

=======
Suggestion 2

def f(n, k):
    for i in range(k):
        if n % 200 == 0:
            n = n // 200
        else:
            n = int(str(n) + "200")
    return n

=======
Suggestion 3

def myfun():
    N,K = input().split()
    N = int(N)
    K = int(K)
    for i in range(K):
        if N % 200 == 0:
            N = int(N / 200)
        else:
            N = int(str(N) + "200")
    print(N)
myfun()

=======
Suggestion 4

def problem200_b():
    # 读取输入
    str = input()
    str = str.split(" ")
    N = int(str[0])
    K = int(str[1])
    # 循环K次
    for i in range(K):
        # 如果N是200的倍数，就用它除以200。
        if N % 200 == 0:
            N = N // 200
        else:
            # 否则，将N看作一个字符串，并在它的末尾加上200。
            N = int(str(N) + "200")
    # 打印出所得的整数
    print(N)

=======
Suggestion 5

def problem200_b():
    N, K = map(int, input().split())
    for i in range(K):
        if N % 200 == 0:
            N = N // 200
        else:
            N = int(str(N) + "200")
    print(N)

=======
Suggestion 6

def problems200_b(n, k):
    for i in range(k):
        if n % 200 == 0:
            n = n // 200
        else:
            n = int(str(n) + '200')
    return n

=======
Suggestion 7

def problem200_b():
    N, K = map(int, input().split())
    for _ in range(K):
        if N % 200 == 0:
            N //= 200
        else:
            N = int(str(N) + '200')
    print(N)

=======
Suggestion 8

def fun(N,K):
    for i in range(K):
        if N%200 == 0:
            N = N // 200
        else:
            N = int(str(N) + '200')
    return N

=======
Suggestion 9

def main():
    N,K = map(int,input().split())
    for i in range(K):
        if N % 200 == 0:
            N = int(N / 200)
        else:
            N = int(str(N) + "200")
    print(N)

=======
Suggestion 10

def main():
    n, k = map(int, input().split())
    for _ in range(k):
        if n % 200 == 0:
            n //= 200
        else:
            n = int(str(n) + '200')
    print(n)
