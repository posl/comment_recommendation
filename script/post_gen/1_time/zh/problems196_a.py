Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(b - c)

=======
Suggestion 2

def get_max_value(a, b, c, d):
    max_value = -10000000000
    for x in range(a, b + 1):
        for y in range(c, d + 1):
            if max_value < x - y:
                max_value = x - y
    return max_value

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max(a-c, a-d, b-c, b-d))

=======
Suggestion 4

def problem196_a():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max(a - c, a - d, b - c, b - d))

problem196_a()

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max(b-c, b-d, a-c, a-d))

=======
Suggestion 6

def main():
    # 读取输入
    a, b = map(int, input().split())
    c, d = map(int, input().split())

    # 求解并输出
    print(max(a-c, a-d, b-c, b-d))

=======
Suggestion 7

def max_x_y(a, b, c, d):
    x = a
    y = c
    if (a + c) < (a + d):
        y = d
    if (a + c) < (b + c):
        x = b
    return x - y

=======
Suggestion 8

def main():
    # 读取输入
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    # 写入输出
    print(max(a - c, a - d, b - c, b - d))
