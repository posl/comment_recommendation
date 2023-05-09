Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, x = map(int, input().split())
    if a*a*b/2 >= x:
        print(90 - math.degrees(math.atan(2*x/(a*b*b))))
    else:
        print(math.degrees(math.atan(2*(a*a*b-x)/(a*a*a))))

=======
Suggestion 2

def solve(a,b,x):
    import math
    if a*a*b/2 >= x:
        return math.degrees(math.atan2(a*b*b,2*x))
    else:
        return math.degrees(math.atan2(2*(a*a*b-x),a*a*a))

=======
Suggestion 3

def main():
    a,b,x = map(int,input().split())
    if x > a*a*b/2:
        print(90 - math.degrees(math.atan(2*(a*a*b-x)/(a*a*a))))
    else:
        print(math.degrees(math.atan(a*b*b/(2*x))))

=======
Suggestion 4

def main():
    a, b, x = map(int, input().split())
    if x <= a**2 * b / 2:
        print(90 - math.degrees(math.atan(2*x/a/b**2)))
    else:
        print(math.degrees(math.atan((2*b/a) - (2*x/a**3))))

=======
Suggestion 5

def main():
    a,b,x = map(int, input().split())
    if x > a*a*b/2:
        print(90 - math.degrees(math.atan(2*(a*a*b-x)/(a*a*a))))
    else:
        print(math.degrees(math.atan((a*b*b)/(2*x))))

=======
Suggestion 6

def main():
    a,b,x = map(int,input().split())
    if x <= a**2*b/2:
        print(90 - math.degrees(math.atan(2*x/a/b**2)))
    else:
        print(math.degrees(math.atan(2*(a**2*b-x)/a**3)))

=======
Suggestion 7

def solve(a, b, x):
    if a*a*b/2 >= x:
        return 90 - 2*x/(a*b*b)*180
    else:
        return 2*(a*a*b-x)/(a*a*a)*180

=======
Suggestion 8

def main():
    a, b, x = map(int, input().split())
    if x > a**2*b/2:
        print(90 - 2*180*atan(2*(a**2*b-x)/(a**3)))
    else:
        print(90 - 180*atan(2*x/(a*b**2)))

=======
Suggestion 9

def find_angle(a, b, x):
    if x > a**2*b/2:
        return 90 - math.atan(2*(a**2*b-x)/(a**3))
    else:
        return math.atan(a*b**2/(2*x))

=======
Suggestion 10

def solve(a,b,x):
    if x >= a*a*b/2:
        return 90 - 180 * (a*a*b-x)/(a*a*a)
    else:
        return 180 * x/(a*b*b)
