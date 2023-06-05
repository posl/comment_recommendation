Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X, Y, R = map(float, input().split())
    X = int(X * 10000)
    Y = int(Y * 10000)
    R = int(R * 10000)
    ans = 0
    for x in range(X - R, X + R + 1):
        d = R * R - (X - x) ** 2
        if d < 0:
            continue
        d = int(d ** 0.5)
        y1 = Y + d
        y2 = Y - d
        ans += (y1 // 10000 - y2 // 10000 + 1)
    print(ans)

=======
Suggestion 2

def main():
    # input
    X, Y, R = map(float, input().split())

    # compute
    X_min = int(X - R)
    X_max = int(X + R)
    Y_min = int(Y - R)
    Y_max = int(Y + R)

    count = 0
    for x in range(X_min, X_max + 1):
        for y in range(Y_min, Y_max + 1):
            if (X - x) ** 2 + (Y - y) ** 2 <= R ** 2:
                count += 1

    # output
    print(count)

=======
Suggestion 3

def main():
    import sys
    import math

    # 读入数据
    data = sys.stdin.readline().strip().split()
    x, y, r = map(float, data)

    # 计算
    x1 = math.floor(x - r)
    x2 = math.ceil(x + r)
    count = 0
    for i in range(x1, x2 + 1):
        y1 = math.floor(y - math.sqrt(r * r - (i - x) * (i - x)))
        y2 = math.ceil(y + math.sqrt(r * r - (i - x) * (i - x)))
        for j in range(y1, y2 + 1):
            if (i - x) * (i - x) + (j - y) * (j - y) <= r * r:
                count += 1

    # 输出结果
    print(count)

=======
Suggestion 4

def main():
    x, y, r = map(float, input().split())
    x = int(x * 10000)
    y = int(y * 10000)
    r = int(r * 10000)
    x1 = x - r
    x2 = x + r
    y1 = y - r
    y2 = y + r
    ans = 0
    for i in range(y1, y2 + 1):
        for j in range(x1, x2 + 1):
            if (i - y) ** 2 + (j - x) ** 2 <= r ** 2:
                ans += 1
    print(ans)

main()

=======
Suggestion 5

def main():
    x, y, r = map(float, input().split())
    x = int(x*10000)
    y = int(y*10000)
    r = int(r*10000)
    x1 = x - r
    x2 = x + r
    y1 = y - r
    y2 = y + r
    ans = 0
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            if (i-x)*(i-x) + (j-y)*(j-y) <= r*r:
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    x,y,r = map(float,input().split())
    x = int(x*10000)
    y = int(y*10000)
    r = int(r*10000)
    r2 = r*r
    ans = 0
    for i in range(-r,r+1):
        j = r2 - i*i
        if j>=0:
            j = int(j**0.5)
            ans += j//10000 +1
    print(ans*4)

=======
Suggestion 7

def main():
    X, Y, R = map(float, input().split())
    X = int(X * 10000)
    Y = int(Y * 10000)
    R = int(R * 10000)
    ans = 0
    for i in range(X - R, X + R + 1):
        if (R ** 2 - (i - X) ** 2) >= 0:
            ans += int((R ** 2 - (i - X) ** 2) ** 0.5) // 10000 + 1
    ans *= 2
    print(ans)

=======
Suggestion 8

def f(x,y,r):
    from math import sqrt
    x1=int(x)
    y1=int(y)
    r1=int(r)
    count=0
    for i in range(x1-r1,x1+r1+1):
        for j in range(y1-r1,y1+r1+1):
            if sqrt((i-x)**2+(j-y)**2)<=r:
                count+=1
    return count

=======
Suggestion 9

def count_grid_points_in_or_on_circle(x,y,r):
    import math
    count = 0
    for i in range(math.floor(x-r),math.ceil(x+r)+1):
        for j in range(math.floor(y-r),math.ceil(y+r)+1):
            if math.sqrt((i-x)**2 + (j-y)**2) <= r:
                count += 1
    return count

=======
Suggestion 10

def get_point_num(x, y, r):
    # print(x, y, r)
    if r.is_integer():
        r = int(r)
    else:
        r = int(r) + 1
    x = int(x * 10000)
    y = int(y * 10000)
    # print(x, y, r)
    # print(r ** 2)
    # print((x - r) ** 2)
    # print((x + r) ** 2)
    # print((y - r) ** 2)
    # print((y + r) ** 2)
    num = 0
    for i in range(x - r, x + r + 1):
        for j in range(y - r, y + r + 1):
            if (i - x) ** 2 + (j - y) ** 2 <= r ** 2:
                num += 1
    return num
