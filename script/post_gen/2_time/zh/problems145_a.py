Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(a,b,x):
    if x <= a*a*b/2:
        # 这种情况下，水的高度小于等于a/2，所以倾斜角度为45°
        return 45
    else:
        # 这种情况下，水的高度大于a/2，所以倾斜角度为
        # tanθ = (a^2*b-x)/(a^3/2)
        # θ = atan((a^2*b-x)/(a^3/2))
        return math.atan((a*a*b-x)/(a*a*a/2))*180/math.pi

=======
Suggestion 2

def main():
    a,b,x = map(int,input().split())
    if a*a*b/2 > x:
        print(90 - math.degrees(math.atan(2*x/(a*b*b))))
    else:
        print(math.degrees(math.atan(2*(a*a*b-x)/(a*a*a))))
    return

=======
Suggestion 3

def getAngle(a, b, x):
    import math
    if (x == a * a * b):
        return 0
    if (x == 0):
        return 90
    if (x == a * a * b / 2):
        return 45
    if (x < a * a * b / 2):
        return math.degrees(math.atan((2 * x) / (a * b * b)))
    if (x > a * a * b / 2):
        return math.degrees(math.atan((2 * (a * a * b - x)) / (a * a * a)))

=======
Suggestion 4

def main():
    a, b, x = map(int, input().split())
    if x >= a * a * b / 2:
        print(90 - (90 - 2 * (b / a) * (b - x / a / a)) * 180 / 3.141592653589793238)
    else:
        print((90 - 2 * x / a / b / b) * 180 / 3.141592653589793238)

=======
Suggestion 5

def f(a,b,x):
    if x == a*a*b:
        return 45
    else:
        return 0

=======
Suggestion 6

def solve(a, b, x):
    import math
    if x >= a*a*b/2:
        ans = math.degrees(math.atan(2*(a*a*b-x)/(a*a*a)))
    else:
        ans = math.degrees(math.atan((a*b*b)/(2*x)))
    return ans

=======
Suggestion 7

def judge(a, b, x, theta):
    if a*a*b/2.0 <= x:
        #瓶子是满的
        #瓶子的体积是a*a*b，水的体积是x，瓶子的倾斜角度是theta
        #瓶子的倾斜角度是theta，瓶子的底面是一个正方形，所以瓶子的倾斜角度是theta的时候，瓶子的底面的边长是a*cos(theta)
        #所以瓶子的倾斜角度是theta的时候，瓶子的水面的面积是a*a*cos(theta)/2
        #所以瓶子的倾斜角度是theta的时候，瓶子的水面的高度是x/(a*a*cos(theta)/2)
        #所以瓶子的倾斜角度是theta的时候，瓶子的水面的高度是2*x/(a*a*cos(theta))
        #所以瓶子的倾斜角度是theta的时候，瓶子的水面的高度是2*x/(a*a*cos(theta))
        #所以瓶子的倾斜角度是theta的时候，瓶子的水面的高度是2*x/(a*a*cos(theta))
        #所以瓶子的倾斜角度是theta的时候，瓶子的水面的高度是2*x/(a*a*cos(theta))
        #所以瓶子的倾斜角度是theta的时候，瓶子的水面的高度是2*x/(a*a*cos(theta))
        #所以瓶子的倾斜角度是theta的时候，瓶子的水面的高度是2*x/(a*a*cos(theta))
        #所以瓶子的倾斜角度是theta的时候，瓶子的水面的高度是2*x

=======
Suggestion 8

def main():
    a,b,x = map(int, input().split())
    if x <= a*a*b/2:
        print(90 - (x/a/a*2)*90)
    else:
        print((2*(a*a*b-x)/a/a/a)*90)

=======
Suggestion 9

def main():
    a,b,x = map(int,input().split())
    if x > a**2 * b / 2:
        ans = math.atan(2*(a**2*b-x)/(a**3))
    else:
        ans = math.atan((a*b**2)/(2*x))
    ans = math.degrees(ans)
    print(ans)

=======
Suggestion 10

def solve(a, b, x):
    import math
    if x <= a * a * b / 2:
        ans = math.atan(a * b * b / 2 / x) * 180 / math.pi
    else:
        ans = math.atan(2 * (b - x / a / a) / a) * 180 / math.pi
    return ans
