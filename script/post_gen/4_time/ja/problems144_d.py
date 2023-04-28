Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a,b,x = map(int, input().split())
    if x <= a*a*b/2:
        ans = 90 - math.degrees(math.atan(2*x/(a*b*b)))
    else:
        ans = math.degrees(math.atan(2*(a*a*b-x)/(a*a*a)))
    print(ans)

=======
Suggestion 2

def main():
    a,b,x = map(int,input().split())

    if x <= a*a*b/2:
        print(90 - math.degrees(math.atan(2*x/(a*b*b))))
    else:
        print(math.degrees(math.atan(2*(a*a*b-x)/(a*a*a))))

=======
Suggestion 3

def solve():
    a, b, x = map(int, input().split())
    if x*2 <= a*a*b:
        print(90 - math.degrees(math.atan(2*x/(a*b*b))))
    else:
        print(math.degrees(math.atan(2*(a*a*b-x)/(a*a*a))))

=======
Suggestion 4

def main():
    a, b, x = map(int, input().split())
    if a*a*b == x:
        print(0)
    elif x <= a*a*b/2:
        print(90 - math.degrees(math.atan(2*x/(a*b*b))))
    else:
        print(math.degrees(math.atan(2*(a*a*b-x)/(a*a*a))))

=======
Suggestion 5

def main():
    a,b,x = map(int,input().split())
    if x <= a**2 * b / 2:
        print(90 - math.degrees(math.atan(2 * x / (a * b**2))))
    else:
        print(math.degrees(math.atan(2 * (a**2 * b - x) / (a**3))))

=======
Suggestion 6

def main():
    a,b,x = map(int,input().split())
    if x <= a*a*b/2:
        print(90 - 2*x/(a*b*b))
    else:
        print(2*(a*a*b-x)/(a*a*a))

=======
Suggestion 7

def solve(a, b, x):
    if x * 2 < a * a * b:
        return math.atan(a * b * b / (2 * x)) * 180 / math.pi
    else:
        return math.atan(2 * (a * a * b - x) / (a * a * a)) * 180 / math.pi

import math
a, b, x = map(int, input().split())
print(solve(a, b, x))

=======
Suggestion 8

def main():
    a,b,x = map(int, input().split())
    if x == a * a * b:
        print(0)
    elif x < a * a * b / 2:
        print(90 - math.degrees(math.atan(2 * x / (a * b * b))))
    else:
        print(math.degrees(math.atan(2 * (a * a * b - x) / (a * a * a))))

=======
Suggestion 9

def solve():
    a, b, x = map(int, input().split())
    if a*a*b/2 <= x:
        return 90 - (a*a*b-x)*2/a/a
    else:
        return 90 - x*2/a/b/b

print(solve())

=======
Suggestion 10

def solve():
    a,b,x = map(int,input().split())
    if x == a*a*b:
        print(0)
    else:
        if x <= a*a*b/2:
            print(90-math.degrees(math.atan2((a*b*b)/2,x)))
        else:
            print(math.degrees(math.atan2((2*(a*a*b-x))/(a*a),a)))
