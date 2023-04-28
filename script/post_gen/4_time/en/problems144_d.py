Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, x = map(int, input().split())
    if x <= a*a*b/2:
        ans = 90 - math.degrees(math.atan(2*x/a/b/b))
    else:
        ans = math.degrees(math.atan(2*(a*a*b-x)/a/a/a))
    print(ans)

=======
Suggestion 2

def main():
    a, b, x = map(int, input().split())
    if x <= a**2 * b / 2:
        print(90 - math.degrees(math.atan(2*x/(a*b**2))))
    else:
        print(math.degrees(math.atan(2*(a**2*b - x)/(a**3))))

=======
Suggestion 3

def solve():
    a, b, x = map(int, input().split())
    if x > a*a*b/2:
        print(90 - math.degrees(math.atan(2*(a*a*b-x)/(a*a*a))))
    else:
        print(math.degrees(math.atan(a*b*b/(2*x))))

=======
Suggestion 4

def main():
    import math
    a, b, x = map(int, input().split())
    if x <= a*a*b/2:
        print(math.atan(a*b*b/2/x)*180/math.pi)
    else:
        print(math.atan((2*b/a-2*x/a/a)*a/b)*180/math.pi)

=======
Suggestion 5

def solve(a, b, x):
    if x <= a*a*b/2:
        return 90 - 2 * math.degrees(math.atan(2*x/(a*b*b)))
    else:
        return math.degrees(math.atan(2*(a*a*b-x)/(a*a*a)))

=======
Suggestion 6

def main():
    a, b, x = map(int, input().split())
    if x >= a*a*b/2:
        print(90 - 180 * (a*a*b - x) / (a*a*a))
    else:
        print(180 * x / (a*b*b))

=======
Suggestion 7

def main():
    import math
    a, b, x = map(int, input().split())
    if x < a**2*b/2:
        print(math.degrees(math.atan2(b, 2*x/a/b)))
    else:
        print(math.degrees(math.atan2(2/a*(b-x/a**2), a)))

=======
Suggestion 8

def solve(a, b, x):
    if x >= a*a*b/2:
        return 90 - 2*(a*a*b-x)/(a*a*a)
    else:
        return 2*x/(a*b*b)

=======
Suggestion 9

def main():
    a,b,x = map(int, input().split())
    if 2*x >= a*a*b:
        print(90 - (90*2*x/(a*a*a - x)))
    else:
        print(90 - (90*2*x/(a*b*b)))

=======
Suggestion 10

def main():
    # get input
    a, b, x = map(int, input().split())

    # calculate
    if x <= a*a*b/2:
        # when x is less than half of the volume, the angle is 90 degrees minus the angle of the triangle
        angle = 90 - math.degrees(math.atan(2*x/a/b/b))
    else:
        # when x is more than half of the volume, the angle is the angle of the triangle
        angle = math.degrees(math.atan(2*(a*a*b-x)/a/a/a))

    # output
    print(angle)
