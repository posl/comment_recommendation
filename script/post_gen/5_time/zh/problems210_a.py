Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, a, x, y = map(int, input().split())
    if n <= a:
        print(n * x)
    else:
        print(a * x + (n - a) * y)

=======
Suggestion 2

def main():
    n, a, x, y = map(int, input().split())
    print(min(n, a) * x + max(n - a, 0) * y)

=======
Suggestion 3

def main():
    N,A,X,Y=map(int,input().split())
    if N<=A:
        print(N*X)
    else:
        print(A*X+(N-A)*Y)

=======
Suggestion 4

def solve():
    n, a, x, y = map(int, input().split())
    if n <= a:
        print(n * x)
    else:
        print(a * x + (n - a) * y)

=======
Suggestion 5

def problems210_a():
    # 读取输入
    n, a, x, y = map(int, input().split())
    # 计算结果
    if n > a:
        result = a * x + (n - a) * y
    else:
        result = n * x
    # 输出结果
    print(result)

=======
Suggestion 6

def problems210_a():
    N,A,X,Y = map(int,input().split())
    if N <= A:
        print(N * X)
    else:
        print(A * X + (N - A) * Y)

=======
Suggestion 7

def main():
    n, a, x, y = input().split()
    n = int(n)
    a = int(a)
    x = int(x)
    y = int(y)

    if n <= a:
        print(n * x)
    else:
        print(a * x + (n - a) * y)

=======
Suggestion 8

def price(n,a,x,y):
    if n <= a:
        return n * x
    else:
        return a * x + (n - a) * y
