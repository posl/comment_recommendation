Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a,b,x = map(int,input().split())
    if a*a*b/2 >= x:
        print(90 - 90*x/(a*a*b))
    else:
        print(90*x*2/(a*b*a) - 90)

=======
Suggestion 2

def solve(a, b, x):
    if a * a * b / 2 > x:
        return math.atan(a * b * b / (2 * x))
    else:
        return math.atan(2 * (a * a * b - x) / (a * a * a))

import math
a, b, x = map(int, input().split())
print(math.degrees(solve(a, b, x)))

=======
Suggestion 3

def main():
    a, b, x = map(int, input().split())
    if x <= a**2*b/2:
        print(90 - 2 * x / (a * b**2) * 180 / math.pi)
    else:
        print(2 * (a**2*b - x) / (a**3) * 180 / math.pi)

=======
Suggestion 4

def main():
    a,b,x = map(int, input().split())
    if a*b*b/2 >= x:
        print(90-(x*2)/(a*b))
    else:
        print((x*2)/(a*a*b-2*x))

=======
Suggestion 5

def main():
    a,b,x = map(int,input().split())
    #水的体积
    v = x/a
    #瓶子的倾斜角度
    import math
    if v < a*b/2:
        #瓶子的倾斜角度
        theta = math.atan2(a*b-2*v,a**2)/(2*math.pi)*360
    else:
        #瓶子的倾斜角度
        theta = math.atan2(2*(a*b-v),b**2)/(2*math.pi)*360
    print(theta)
    return

=======
Suggestion 6

def main():
    a,b,x = map(int,input().split())
    if x*2 >= a**2*b:
        print(90)
    else:
        print(90 - math.degrees(math.atan(2*x/(a*b**2))))

=======
Suggestion 7

def main():
    a,b,x = map(int,input().split())
    if x <= a*a*b/2:
        print(90-2*x/(a*b*b))
    else:
        print(2*(a*a*b-x)/(a*a*a))

=======
Suggestion 8

def solve(a,b,x):
    if x == a * a * b:
        return 0
    if x > a * a * b / 2:
        return 90 - solve(a,b,a * a * b - x)
    return solve(b,a * a * b - x,b * b * a)

=======
Suggestion 9

def solve(a,b,x):
    import math
    if a*a*b/2.0 > x:
        return math.atan(a*b*b/2.0/x)/math.pi*180
    else:
        return math.atan(2*(b-x/(a*a))/a)/math.pi*180

=======
Suggestion 10

def main():
    a,b,x = map(int, input().split())
    if a*a*b/2 < x:
        print(90 - 180*2*(a*a*b-x)/(a*a*a))
    else:
        print(180*2*x/(a*b*b))
