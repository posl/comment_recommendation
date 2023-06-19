Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    n = b - a
    print(int(n*(n-1)/2 - a))

=======
Suggestion 2

def solve(a, b):
    # 两座塔之间的距离
    distance = b - a
    # 雪覆盖的深度
    depth = 0
    # 从1开始，逐个增加雪覆盖深度，直到满足条件
    for i in range(1, distance+1):
        depth += i
        if depth >= distance:
            break
    return depth - distance

=======
Suggestion 3

def solve():
    a,b = map(int,input().split())
    h = b - a
    x = 1
    while x*(x+1)//2 < h:
        x += 1
    print(x*(x+1)//2 - h)

=======
Suggestion 4

def snow(a,b):
    n = b-a
    count = 0
    for i in range(1,n+1):
        count += i
    return count - a

=======
Suggestion 5

def main():
    a,b = input().split()
    a = int(a)
    b = int(b)
    x = b - a
    i = 1
    while True:
        if i*(i+1)/2 >= x:
            break
        i += 1
    print(int(i*(i+1)/2-x))

=======
Suggestion 6

def snow(a,b):
    return b-a

=======
Suggestion 7

def calc(a, b):
    # 1+2+3+...+n = n(n+1)/2
    # 1+2+3+...+n+m = (n+m)(n+m+1)/2 - n(n+1)/2
    #               = (2n+m)(m+1)/2
    # 1+2+3+...+n+m+1 = (n+m+1)(n+m+2)/2 - (n+m)(n+m+1)/2
    #                 = (2n+2m+1)(m+1)/2
    # 1+2+3+...+n+m+2 = (n+m+2)(n+m+3)/2 - (n+m+1)(n+m+2)/2
    #                 = (2n+2m+3)(m+1)/2
    # 1+2+3+...+n+m+3 = (n+m+3)(n+m+4)/2 - (n+m+2)(n+m+3)/2
    #                 = (2n+2m+5)(m+1)/2
    # ...
    # 1+2+3+...+n+m+i = (2n+2m+2i+1)(m+1)/2
    # ...
    # 1+2+3+...+n+m+k = (2n+2m+2k+1)(m+1)/2
    # 1+2+3+...+n+m+k+1 = (2n+2m+2k+3)(m+1)/2
    # 1+2+3+...+n+m+k+2 = (2n+2m+2k+5)(m+1)/2
    # 1+2+3+...+n+m+k+3 = (2n+2m+2k+7)(m+1)/2
    # ...
    # 1+2+3+...+n+m+k+m = (2n+2m+4k+2m+1)(m+1)/2
    #                   = (2n+4m+4k+1)(m+1)/2
    #                   = (2n+

=======
Suggestion 8

def get_snow_cover(a, b):
    return b - a - 1

=======
Suggestion 9

def solution(a,b):
    #计算雪覆盖的深度
    #两座塔的高度分别为10米和15米。
    #因此，我们可以看到，雪覆盖的深度是2米。
    return b-a-1
