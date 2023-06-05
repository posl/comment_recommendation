Synthesizing 10/10 solutions

=======
Suggestion 1

def get_distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

=======
Suggestion 2

def problems246_b():
    a, b = map(int, input().split())
    print(b / (a ** 2 + b ** 2) ** 0.5, a / (a ** 2 + b ** 2) ** 0.5)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if a == 0:
        print('0 1')
    elif b == 0:
        print('1 0')
    else:
        x = a / (a + b)
        y = b / (a + b)
        print(x, y)

=======
Suggestion 4

def main():
    a,b = map(int,input().split())
    x = 1
    y = 0
    while True:
        if x**2 + y**2 > a**2 + b**2:
            break
        x += 1
        y += 1
    x -= 1
    y -= 1
    if x == 0:
        x = 1
    print((x*a)/((x**2+y**2)**0.5),(y*b)/((x**2+y**2)**0.5))

=======
Suggestion 5

def main():
    a,b = map(int, input().split())
    x = a/(a**2+b**2)**0.5
    y = b/(a**2+b**2)**0.5
    print(x,y)

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    x = a * 1.0 / (a * a + b * b) ** 0.5
    y = b * 1.0 / (a * a + b * b) ** 0.5
    print(x, y)

=======
Suggestion 7

def problem246_b():
    pass

=======
Suggestion 8

def main():
    # 读入数据
    A, B = map(int, input().split())
    # 计算结果
    x = A / (A ** 2 + B ** 2) ** 0.5
    y = B / (A ** 2 + B ** 2) ** 0.5
    # 输出结果
    print(x, y)
    # print("{:.12f} {:.12f}".format(x, y))

=======
Suggestion 9

def problem246_b():
    a, b = map(int, input().split())
    x = a / (a**2 + b**2)**0.5
    y = b / (a**2 + b**2)**0.5
    print(x, y)

problem246_b()

=======
Suggestion 10

def solve():
    import math
    A, B = map(int, input().split())
    x = 0
    y = 0
    d = math.sqrt(A**2 + B**2)
    x = x + A/d
    y = y + B/d
    print("{0:.12f} {1:.12f}".format(x, y))
