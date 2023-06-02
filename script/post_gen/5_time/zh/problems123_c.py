Synthesizing 10/10 solutions

=======
Suggestion 1

def problem123_c():
    return 0

=======
Suggestion 2

def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    print((n-1)//min(a,b,c,d,e)+5)

=======
Suggestion 3

def problem123_c():
    pass

=======
Suggestion 4

def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    print(5 + (n-1)//min(a, b, c, d, e))

=======
Suggestion 5

def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    print(4 + (n - 1) // min(a, b, c, d, e))

=======
Suggestion 6

def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    print(4 + (n + min(a, b, c, d, e) - 1) // min(a, b, c, d, e))
    return

=======
Suggestion 7

def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    #计算最少时间
    #最少时间是：最多人数／交通工具的最大载客量
    #最多人数是：n／交通工具的最少运行次数
    #交通工具的最少运行次数是：交通工具的最大载客量／交通工具的最少载客量
    #交通工具的最大载客量是：交通工具的最少载客量的整数倍（取整）

    #交通工具的最少载客量
    min_load = min(a,b,c,d,e)
    #交通工具的最大载客量
    max_load = max(a,b,c,d,e)
    #交通工具的最少运行次数
    min_run = int(max_load/min_load)
    #最多人数
    max_people = min_run*n
    #最少时间
    min_time = int(max_people/max_load)
    if max_people%max_load != 0:
        min_time += 1

    print(min_time)

=======
Suggestion 8

def f(n,a,b,c,d,e):
    return (n-1)//min(a,b,c,d,e)+5

n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
print(f(n,a,b,c,d,e))

=======
Suggestion 9

def problem123_c():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    print(5 + (n - 1) // min(a, b, c, d, e))
problem123_c()

=======
Suggestion 10

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    min = A
    if min > B:
        min = B
    if min > C:
        min = C
    if min > D:
        min = D
    if min > E:
        min = E
    print(int(4 + (N + min - 1) / min))
