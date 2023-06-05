Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, x = map(int, input().split())
    if x <= a*a*b/2:
        print(90 - math.degrees(math.atan(2*x/(a*b*b))))
    else:
        print(math.degrees(math.atan(2*(a*a*b-x)/(a*a*a))))

=======
Suggestion 2

def solve(a,b,x):
    import math
    if x >= a*a*b/2:
        return math.atan(2*(a*a*b-x)/(a*a*a))*180/math.pi
    else:
        return math.atan(a*b*b/(2*x))*180/math.pi

=======
Suggestion 3

def main():
    a,b,x = map(int, input().split())
    if x >= a*a*b/2:
        print(90 - 90*2*(x-a*a*b/2)/(a*a*a))
    else:
        print(90*2*x/(a*b*b))

=======
Suggestion 4

def solve(a, b, x):
    if x > a * a * b / 2:
        return 90 - solve(a, b, a * a * b - x)
    return math.degrees(math.atan(2 * x / a / b / b))

a, b, x = map(int, input().split())
print(solve(a, b, x))

=======
Suggestion 5

def solve(a, b, x):
    if a*a*b/2.0 >= x:
        return math.atan(a*b*b/2.0/x)/math.pi*180.0
    else:
        return math.atan(2.0*(a*a*b-x)/(a*a*a))/math.pi*180.0

=======
Suggestion 6

def calcAngle(a, b, x):
    return 90 - math.degrees(math.atan(2 * x / b / a ** 2))

import math
a, b, x = map(int, input().split())

=======
Suggestion 7

def main():
    a,b,x = map(int,input().split())
    s = x/a
    if 2*s >= a*b:
        print(90-2*(a*b-x)/(a**3))
    else:
        print(2*s/b)

=======
Suggestion 8

def solve(a,b,x):
    return 0

=======
Suggestion 9

def main():
    a,b,x = map(int,input().split())
    if x > a**2*b/2:
        print(90 - 2*(a**2*b-x)/a**3)
    else:
        print(2*x/(a*b**2))

=======
Suggestion 10

def main():
    a, b, x = map(int, input().split())
    if x <= a*a*b/2:
        ans = 90 - math.degrees(math.atan(2*x/a/b/b))
    else:
        ans = math.degrees(math.atan(2*(a*a*b-x)/a/a/a))
    print(ans)
