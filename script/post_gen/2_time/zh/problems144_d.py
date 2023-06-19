Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a,b,x = map(int,input().split())
    if x <= a*a*b/2:
        print(90 - (x*2)/(a*b*b))
    else:
        print((x*2)/(a*a*a) - 90)

=======
Suggestion 2

def solve(a, b, x):
    # 二分法
    # 水的体积
    water = x / a
    # 水的高度
    h = water / a * 2
    # 二分法
    left = 0
    right = 90
    while right - left > 0.0000000001:
        mid = (left + right) / 2
        # 角度转弧度
        rad = mid * 3.14159265358979323846264338327950288 / 180
        # 水的高度
        h = b * math.tan(rad)
        # 水的体积
        water = a * a * b - a * a * h / 2
        # 比较
        if water > x:
            right = mid
        else:
            left = mid
    return mid

a, b, x = map(int, input().split())
print(solve(a, b, x))

=======
Suggestion 3

def f(a, b, x):
    if x <= a*a*b/2:
        return 90 - (x*2)/(a*b)
    else:
        return (a*a*b - x)*2/(a*a)

a, b, x = map(int, input().split())
print(f(a, b, x))

=======
Suggestion 4

def main():
    a,b,x = map(int, input().split())
    if x <= a*a*b/2:
        print(90 - (x*2)/(a*b*b))
    else:
        print((x*2)/(a*a) - (b/2))

=======
Suggestion 5

def main():
    a, b, x = map(int, input().split())
    if x <= a*a*b/2:
        print(90 - 2*x/a/a/b*180)
    else:
        print(2*(a*a*b-x)/a/a/a*180)

=======
Suggestion 6

def main():
    a,b,x = map(int,input().split())
    if x > a**2*b/2:
        print(90 - 90*2*x/(a**3-2*x))
    else:
        print(90*x/a**2/b*2)

=======
Suggestion 7

def main():
    #读取数据
    a,b,x = map(int,input().split())
    #计算
    if x >= a**2*b/2:
        #当水满的时候，计算
        h = (a**2*b-x)*2/a**2
        #计算角度
        import math
        ans = math.atan2(h,a)
        #转换为角度
        ans = ans*180/math.pi
    else:
        #当水不满的时候，计算
        h = x*2/a/b
        #计算角度
        import math
        ans = math.atan2(b,h)
        #转换为角度
        ans = ans*180/math.pi
    #打印结果
    print(ans)

=======
Suggestion 8

def main():
    a,b,x=map(int,input().split())
    if x<=a*a*b/2:
        print(90-90*x/(a*a*b))
    else:
        print(90*x/(a*a*a)-90*a*b/(2*a*a*a-2*x))

=======
Suggestion 9

def solve(a, b, x):
    if x > a*a*b/2:
        return 90 - solve(a, b, a*a*b-x)
    else:
        return 90 - math.degrees(math.atan(2*x/(a*b*b)))

import math
a, b, x = map(int, input().split())
print(solve(a, b, x))

=======
Suggestion 10

def get_angle(a, b, x):
    if x > a * a * b / 2:
        return 90 - get_angle(a, b, a * a * b - x)
    return math.degrees(math.atan(2 * x / a / b / b))

import math
a, b, x = map(int, input().split())
print(get_angle(a, b, x))
