Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(a, b, x):
    if x >= a * a * b / 2:
        return 90 - solve(a, b, a * a * b - x)
    return math.atan2(2 * x, a * b * b) * 180 / math.pi

=======
Suggestion 2

def main():
    a,b,x = map(int, input().split())
    if x < a*a*b/2:
        ans = 90 - math.degrees(math.atan(2*x/(a*b*b)))
    else:
        ans = math.degrees(math.atan(2*(a*a*b-x)/(a*a*a)))
    print(ans)

=======
Suggestion 3

def main():
    import math
    a,b,x = map(int,input().split())
    if x <= a*a*b/2:
        ans = math.atan((b*b*a)/(2*x))
    else:
        ans = math.atan((2*b - (2*x)/(a*a)) / a)
    print(math.degrees(ans))

=======
Suggestion 4

def solve(a, b, x):
    import math
    if x > a*a*b/2:
        return math.atan(2*(a*a*b-x)/(a*a*a))
    else:
        return math.atan((a*b*b)/(2*x))

=======
Suggestion 5

def main():
    a,b,x = map(int,input().split())
    if x >= a*a*b/2:
        print(90 - 2*(a*a*b-x)/(a*a*a))
    else:
        print(2*x/(a*b*b))

=======
Suggestion 6

def main():
    a,b,x = map(int, input().split())
    if x >= a*a*b/2:
        print(90 - 90*2*(a*a*b-x)/(a*a*a))
    else:
        print(90*2*x/(a*b*b))

=======
Suggestion 7

def solve():
    a, b, x = map(int, input().split())
    if x <= a*a*b/2:
        ans = 90 - math.degrees(math.atan(2*x/(a*b*b)))
    else:
        ans = math.degrees(math.atan(2*(a*a*b-x)/(a*a*a)))
    print(ans)

=======
Suggestion 8

def solve(a, b, x):
    import math
    if x <= (a ** 2 * b) / 2:
        return math.degrees(math.atan((a * b ** 2) / (2 * x)))
    else:
        return math.degrees(math.atan(2 * (a ** 2 * b - x) / (a ** 3)))

=======
Suggestion 9

def solve(a,b,x):
    import math
    if a*a*b/2 > x:
        return math.degrees(math.atan(a*b*b/(2*x)))
    else:
        return math.degrees(math.atan(2*(a*a*b-x)/(a*a*a)))

=======
Suggestion 10

def main():
    a,b,x=map(int,input().split())
    if x<=a*a*b/2:
        ans=90-2*x/(a**3)*180
    else:
        ans=2*(a**2*b-x)/(a**2)*180
    print(ans)
