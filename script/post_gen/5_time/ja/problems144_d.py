Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b,x = map(int,input().split())
    if x <= a**2*b/2:
        ans = 90 - math.degrees(math.atan(2*x/(a*b**2)))
    else:
        ans = math.degrees(math.atan(2*(a**2*b-x)/(a**3)))
    print(ans)

=======
Suggestion 2

def main():
    a,b,x = map(int,input().split())
    if a*a*b/2 >= x:
        print(90 - math.degrees(math.atan((2*x)/(a*b*b))))
    else:
        print(math.degrees(math.atan(2*(a*a*b-x)/(a*a*a))))

=======
Suggestion 3

def main():
    a,b,x = map(int,input().split())
    if a*a*b/2 <= x:
        ans = 90 - (a*a*b-x)*2/(a*a*a)
    else:
        ans = (a*b*b)/(2*x)
    print(ans)

=======
Suggestion 4

def main():
    a,b,x = map(int,input().split())
    if a*a*b/2 < x:
        print(90 - math.degrees(math.atan(2*(a*a*b-x)/(a*a*a))))
    else:
        print(math.degrees(math.atan(a*b*b/(2*x))))

=======
Suggestion 5

def solve():
    a,b,x = map(int,input().split())
    if x > a*a*b/2:
        print(90 - 2*(a*a*b-x)/a/a/a)
    else:
        print(2*x/b/a/b)

=======
Suggestion 6

def main():
    a,b,x = map(int, input().split())
    if x >= a*a*b/2:
        ans = 90 - math.degrees(math.atan(2*(a*a*b-x)/(a*a*a)))
    else:
        ans = math.degrees(math.atan(a*b*b/(2*x)))
    print(ans)

=======
Suggestion 7

def main():
    a,b,x = map(int,input().split())
    if x >= a**2 * b / 2:
        ans = 90 - math.degrees(math.atan(2*(a**2*b-x)/(a**3)))
    else:
        ans = math.degrees(math.atan(a*b**2/(2*x)))
    print(ans)

=======
Suggestion 8

def main():
    a, b, x = map(int, input().split())
    if x >= a**2 * b / 2:
        print(90 - (90 * 2 * (a**2 * b - x) / (a**3)))
    else:
        print(90 * (x * 2 / (a * b)) / (b))

=======
Suggestion 9

def solve(a,b,x):
    if x*2 <= a*a*b:
        return 90 - math.degrees(math.atan(x*2/(a*b*b)))
    else:
        return math.degrees(math.atan((a*a*b-x)*2/(a*a*a)))

import math
a,b,x = map(int,input().split())
print(solve(a,b,x))
