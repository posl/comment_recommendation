Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X, Y, R = map(float, input().split())
    X = int(X * 10000)
    Y = int(Y * 10000)
    R = int(R * 10000)
    ans = 0
    for i in range(X - R, X + R + 1):
        for j in range(Y - R, Y + R + 1):
            if (X - i) ** 2 + (Y - j) ** 2 <= R ** 2:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def get_input():
    input_str = input()
    input_str = input_str.split()
    return input_str

=======
Suggestion 4

def solve():
    X, Y, R = map(float, input().split())
    X = int(X * 10000)
    Y = int(Y * 10000)
    R = int(R * 10000)
    ans = 0
    for x in range(X - R, X + R + 1):
        if (X - x) ** 2 > R ** 2:
            continue
        y = Y + (R ** 2 - (X - x) ** 2) ** 0.5
        while y > Y - 1:
            if x ** 2 + y ** 2 <= R ** 2:
                break
            y -= 1
        y = int(y)
        ans += y - (Y - 1)
    print(ans * 4)

=======
Suggestion 5

def main():
    x, y, r = map(float, input().split())
    x, y, r = int(x*10000), int(y*10000), int(r*10000)
    ans = 0
    for i in range(-r, r+1):
        j = int((r**2 - i**2)**0.5)
        while i**2 + j**2 > r**2:
            j -= 1
        ans += j*2+1
    print(ans*4)

=======
Suggestion 6

def main():
    x,y,r = map(float,input().split())
    x = int(x*10000)
    y = int(y*10000)
    r = int(r*10000)
    ans = 0
    for i in range(x-r,x+r+1):
        for j in range(y-r,y+r+1):
            if (i-x)**2 + (j-y)**2 <= r**2:
                ans += 1
    print(ans)

=======
Suggestion 7

def solve(x, y, r):
    x1 = int(x * 10000 - r * 10000)
    x2 = int(x * 10000 + r * 10000)
    y1 = int(y * 10000 - r * 10000)
    y2 = int(y * 10000 + r * 10000)
    ans = 0
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if (i - x * 10000) ** 2 + (j - y * 10000) ** 2 <= r * 10000 ** 2:
                ans += 1
    return ans

=======
Suggestion 8

def main():
    x,y,r = map(float, input().split())
    x,y,r = int(x*10000), int(y*10000), int(r*10000)
    x1 = int((x-r)/10000)
    x2 = int((x+r)/10000)
    cnt = 0
    for i in range(x1, x2+1):
        y1 = int((r**2 - (i*10000-x)**2)**0.5/10000)
        y2 = int(-(r**2 - (i*10000-x)**2)**0.5/10000)
        cnt += y1 - y2 + 1
    print(cnt)

=======
Suggestion 9

def main():
    import sys
    import math

    # 读入数据
    x, y, r = map(float, sys.stdin.readline().split())

    # 计算答案
    # 在圆内或圆上的网格点的数量
    # = 在圆内的网格点的数量
    # + 在圆上的网格点的数量
    # = 在圆内的网格点的数量
    # + 在圆的边界上的网格点的数量
    # = 在圆内的网格点的数量
    # + 在圆的边界上的网格点的数量
    # = 在圆内的网格点的数量
    # + 在圆的边界上的网格点的数量

    # 在圆内的网格点的数量
    # = 在圆内的网格点的数量
    # + 在圆内的网格点的数量
    # = 在圆内的网格点的数量
    # + 在圆内的网格点的数量
    # = 在圆内的网格点的数量
    # + 在圆内的网格点的数量
    # = 在圆内的网格点的数量
    # + 在圆内的网格点的数量
    # = 在圆内的网格点的数量
    # + 在圆内的网格点的数量
    # = 在圆内的网格点的数量
    # + 在圆内的网格点的数量
    # = 在圆内的网格点的数量
    # + 在圆内的网格点的数量

    # 在圆内的网格点的数量
    # = 在圆内的网格点的数量
    # + 在圆内的网格点的数量
    # = 在圆内的网格点的数量
    # + 在圆内的网格点的数量
    # = 在圆内的网格点的数量

    # 在圆内的网格点的数量
    # = 在圆内的网格点的

=======
Suggestion 10

def main():
    X, Y, R = map(float, input().split())
    X = int(X * 10000)
    Y = int(Y * 10000)
    R = int(R * 10000)
    ans = 0
    for i in range(X - R, X + R + 1):
        for j in range(Y - R, Y + R + 1):
            if (i - X) ** 2 + (j - Y) ** 2 <= R ** 2:
                ans += 1
    print(ans)
