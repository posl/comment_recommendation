Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, x = map(int, input().split())
    if a * a * b / 2 <= x:
        print(90 - math.degrees(math.atan(2 * (a * a * b - x) / a ** 3)))
    else:
        print(math.degrees(math.atan(a * b * b / (2 * x))))

=======
Suggestion 2

def solve(a, b, x):
    if x >= a * a * b / 2:
        return math.degrees(math.atan(2 * (a * a * b - x) / (a * a * a)))
    else:
        return math.degrees(math.atan(a * b * b / (2 * x)))

a, b, x = map(int, input().split())
print(solve(a, b, x))

=======
Suggestion 3

def   main (): 
     a ,   b ,   x   =   map ( int ,   input (). split ()) 
     if   x   >=   a   **   2   *   b   /   2 : 
         print ( 90   -   math . degrees ( math . atan ( 2   *   ( a   **   2   *   b   -   x )   /   ( a   **   3 )))) 
     else : 
         print ( math . degrees ( math . atan ( a   *   b   **   2   /   2   /   x )))

=======
Suggestion 4

def main():
    a, b, x = map(int, input().split())
    if x >= a * a * b / 2:
        h = (a * a * b - x) * 2 / a / a
        print(math.degrees(math.atan2(b - h, a)))
    else:
        h = x * 2 / a / b
        print(math.degrees(math.atan2(b, a - h)))

=======
Suggestion 5

def solve(a,b,x):
    if x <= a*a*b/2:
        return math.degrees(math.atan(2*x/(a*a*b)))
    else:
        return math.degrees(math.atan(2*(a*a*b-x)/(a*a*a)))

a,b,x = map(int,input().split())
print(solve(a,b,x))

import math
a,b,x = map(int,input().split())

=======
Suggestion 6

def main():
    a, b, x = map(int, input().split())
    if x <= a**2*b/2:
        ans = math.degrees(math.atan((2*x)/(a*b**2)))
    else:
        ans = math.degrees(math.atan((a*b**2-2*x)/(a**2*b)))
    print(ans)

=======
Suggestion 7

def main():
    a, b, x = map(int, input().split())
    if x >= a*a*b/2:
        print(90 - math.degrees(math.atan(2*(a*a*b - x)/(a*a*a))))
    else:
        print(math.degrees(math.atan(a*b*b/(2*x))))

=======
Suggestion 8

def main():
    a,b,x = map(int,input().split())
    if x < a**2*b/2:
        print(90-180/math.pi*math.atan(2*x/(a**3)))
    else:
        print(180-180/math.pi*math.atan(2*(a**2*b-x)/(a**3)))

=======
Suggestion 9

def main():
    import math
    a, b, x = map(int, input().split())
    if x > a**2 * b / 2:
        # 三角形
        x = a**2 * b - x
        h = x / (a**2)
        rad = math.atan(2 * h / a)
    else:
        # 二等辺三角形
        h = x * 2 / (a**2)
        rad = math.atan(a / 2 / h)
    print(math.degrees(rad))

=======
Suggestion 10

def main():
    a, b, x = map(int, input().split())
    if x >= a**2*b/2:
        #print('x >= a**2*b/2')
        #print('x = ', x)
        #print('a**2*b/2 = ', a**2*b/2)
        #print('x/a**2 = ', x/a**2)
        #print('b-x/a**2 = ', b-x/a**2)
        print(90 - math.degrees(math.atan2(2*(a**2*b-x), a**3)))
    else:
        #print('x < a**2*b/2')
        #print('x = ', x)
        #print('a**2*b/2 = ', a**2*b/2)
        #print('2*x/a/b = ', 2*x/a/b)
        #print('b**2-2*x/a/b = ', b**2-2*x/a/b)
        print(math.degrees(math.atan2(b**2-2*x/a/b, 2*x/a)))
