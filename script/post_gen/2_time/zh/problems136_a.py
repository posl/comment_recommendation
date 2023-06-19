Synthesizing 10/10 solutions

=======
Suggestion 1

def pour_water(a,b,c):
    if c <= a - b:
        return 0
    else:
        return c - (a - b)

=======
Suggestion 2

def main():
    # 读取输入
    a, b, c = map(int, input().split())
    # 求解并输出
    print(max(0, c - (a - b)))

=======
Suggestion 3

def main():
    a,b,c = map(int,input().split())
    if c <= a - b:
        print(c)
    else:
        print(a-b)

=======
Suggestion 4

def main():
    # 读取输入
    A, B, C = map(int, input().split())
    # 算法
    if A >= B + C:
        print(0)
    else:
        print(C - (A - B))

=======
Suggestion 5

def main():
    A,B,C = map(int,input().split())
    print(max(0,C-(A-B)))

=======
Suggestion 6

def main():
    # 读取输入
    A, B, C = map(int, input().split())
    # 从B瓶中移动到A瓶中
    B = B + C
    # 从A瓶中移动到B瓶中
    C = B - A
    # 从B瓶中移动到A瓶中
    B = B - C

    # 输出结果
    print(C)

=======
Suggestion 7

def main():
    a, b, c = map(int, input().split())
    print(c - (a - b) if c > a - b else c)

=======
Suggestion 8

def main():
    a, b, c = map(int, input().split())
    print(c - (a - b) if a - b < c else 0)

=======
Suggestion 9

def main():
    a, b, c = map(int, input().split())
    print(c - (a - b) if c >= a - b else c)

=======
Suggestion 10

def main():
    # 读取输入
    a,b,c = map(int, input().split())
    # 计算最多能转移多少水
    max_water = a - b
    # 如果2号瓶的水量小于等于最多能转移的水量
    if c <= max_water:
        # 2号瓶的水量为0
        c = 0
    # 否则
    else:
        # 2号瓶的水量为2号瓶的水量减去最多能转移的水量
        c = c - max_water
    # 打印2号瓶的水量
    print(c)
