Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,x,t = map(int, input().split())
    print(int((n+x-1)/x*t))

=======
Suggestion 2

def problem176_a():
    n,x,t = map(int,input().split())
    if n % x == 0:
        print(n//x*t)
    else:
        print((n//x+1)*t)

=======
Suggestion 3

def main():
    n, x, t = map(int, input().split())
    print((n + x - 1) // x * t)

=======
Suggestion 4

def solve():
    n,x,t = map(int,input().split())
    if n%x == 0:
        print(n//x*t)
    else:
        print((n//x+1)*t)

=======
Suggestion 5

def main():
    # 读入数据
    n, x, t = map(int, input().split())
    # 计算结果
    if n % x == 0:
        result = int(n / x) * t
    else:
        result = (int(n / x) + 1) * t
    # 输出结果
    print(result)

=======
Suggestion 6

def main():
    n,x,t=map(int,input().split())
    if n%x==0:
        print(n//x*t)
    else:
        print((n//x+1)*t)

=======
Suggestion 7

def main():
    N, X, T = map(int, input().split())
    num = N // X
    if N % X != 0:
        num += 1
    print(num * T)
