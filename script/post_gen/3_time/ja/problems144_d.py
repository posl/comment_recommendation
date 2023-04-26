Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, x = map(int, input().split())
    if x < a * a * b / 2:
        print(math.degrees(math.atan(2 * x / (a * a * b))))
    else:
        print(math.degrees(math.atan(2 * (a * a * b - x) / (a * a * a))))

=======
Suggestion 2

def main():
    a, b, x = map(int, input().split())
    if x < a * a * b / 2:
        print(math.degrees(math.atan(a * b * b / 2 / x)))
    else:
        print(math.degrees(math.atan(2 * (a * a * b - x) / (a * a * a))))

=======
Suggestion 3

def main():
    a, b, x = map(int, input().split())
    if x < a * a * b / 2:
        ans = math.degrees(math.atan(2 * x / (a * a * b)))
    else:
        ans = math.degrees(math.atan(a * b * b / (2 * x)))
    print(ans)

=======
Suggestion 4

def main():
    a, b, x = map(int, input().split())
    if x >= a * a * b / 2:
        print(90 - math.degrees(math.atan(2 * (a * a * b - x) / (a * a * a))))
    else:
        print(math.degrees(math.atan(a * b * b / (2 * x))))

=======
Suggestion 5

def main():
    a, b, x = map(int, input().split())
    if x <= a * a * b / 2:
        print(90 - math.degrees(math.atan(a * b * b / (2 * x))))
    else:
        print(math.degrees(math.atan(2 * (a * a * b - x) / (a * a * a))))

=======
Suggestion 6

def main():
    a, b, x = map(int, input().split())
    if a * a * b / 2 <= x:
        print(180 * math.atan(2 * (a * a * b - x) / (a * a * a)) / math.pi)
    else:
        print(180 * math.atan(a * b * b / (2 * x)) / math.pi)

=======
Suggestion 7

def main():
    a, b, x = map(int, input().split())
    if x < a**2 * b / 2:
        h = (2 * x) / (a * b)
        print(math.degrees(math.atan(b / h)))
    else:
        h = (2 * (a**2 * b - x)) / (a * b)
        print(math.degrees(math.atan(h / a)))

=======
Suggestion 8

def main():
    a, b, x = map(int, input().split())
    if x < a*a*b/2:
        h = 2*x/(a*b)
        print(math.degrees(math.atan2(b-h, a)))
    else:
        h = 2*(a*a*b-x)/(a*a)
        print(math.degrees(math.atan2(b-h, a)))

=======
Suggestion 9

def main():
    a,b,x=map(int,input().split())
    if x/a**2<=b/2:
        print(degrees(atan(2*x/a**3)))
    else:
        print(degrees(atan(2*b/a-x/a**2)))

=======
Suggestion 10

def main():
    #入力
    a,b,x = map(int,input().split())
    #解答
    if x <= a**2*b/2:
        ans = math.degrees(math.atan(2*x/a**2/b))
    else:
        ans = math.degrees(math.atan(2*(a**2*b-x)/a**3))
    #出力
    print(ans)
