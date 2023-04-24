Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, x = map(int, input().split())
    if x <= a*a*b/2:
        print(math.degrees(math.atan(2*x/(a*a*b))))
    else:
        print(math.degrees(math.atan((a*a*b-x)*2/a/a/a)))

=======
Suggestion 2

def main():
    a, b, x = map(int, input().split())
    if x <= a*a*b/2:
        print(math.degrees(math.atan(2*x/(a*a*b))))
    else:
        print(math.degrees(math.atan(2*(a*a*b-x)/(a*a*a))))

=======
Suggestion 3

def main():
    a, b, x = map(int, input().split())
    if x <= a*a*b/2:
        print(math.degrees(math.atan(2*x/(a*a*b))))
    else:
        print(math.degrees(math.atan(a*b*b/(2*(a*a*b-x)))))

=======
Suggestion 4

def main():
    a, b, x = map(int, input().split())
    if x <= a**2*b/2:
        ans = math.degrees(math.atan(2*x/(a**2*b)))
    else:
        ans = math.degrees(math.atan(2*(a**2*b-x)/(a**3)))
    print(ans)

=======
Suggestion 5

def main():
    a, b, x = map(int, input().split())
    if a * a * b / 2 >= x:
        print(90 - math.degrees(math.atan(2 * x / (a * a * b))))
    else:
        print(math.degrees(math.atan(2 * (a * a * b - x) / (a * a * a))))

=======
Suggestion 6

def solve(a, b, x):
    if x <= a * a * b / 2:
        return math.degrees(math.atan(2 * x / (a * a * b)))
    else:
        return math.degrees(math.atan(2 * (a * a * b - x) / (a * a * a)))

=======
Suggestion 7

def main():
    a,b,x = map(int,input().split())
    if x <= a*a*b/2:
        print(math.degrees(math.atan(2*x/(a*a*b))))
    else:
        print(math.degrees(math.atan(2*a*a*b-2*x)/(a*a)))

=======
Suggestion 8

def main():
    a, b, x = map(int, input().split())
    if x <= a * a * b / 2:
        ans = math.degrees(math.atan((2 * x) / (a * a * b)))
    else:
        ans = math.degrees(math.atan((2 * (a * a * b - x)) / (a * a * a)))
    print(ans)

=======
Suggestion 9

def main():
    a, b, x = map(int, input().split())
    if x <= a**2 * b / 2:
        print(math.degrees(math.atan(2 * x / (a * b**2))))
    else:
        print(math.degrees(math.atan(2 * (a**2 * b - x) / (a**3 * b))))

=======
Suggestion 10

def main():
    a, b, x = map(int, input().split())
    if x > a * a * b / 2:
        theta = math.atan((2 * (a * a * b - x) / (a * a * a)))
    else:
        theta = math.atan((a * b * b) / (2 * x))
    print(math.degrees(theta))
