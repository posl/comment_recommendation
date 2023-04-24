Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, x = map(int, input().split())
    if x > a ** 2 * b / 2:
        h = (a ** 2 * b - x) * 2 / a ** 2
        print(math.degrees(math.atan(b / h)))
    else:
        h = x * 2 / a / b
        print(math.degrees(math.atan(h / a)))

=======
Suggestion 2

def main():
    a, b, x = map(int, input().split())
    if x >= a**2 * b / 2:
        print(90 - math.degrees(math.atan(2 * (a**2 * b - x) / a**3)))
    else:
        print(math.degrees(math.atan(a * b**2 / 2 / x)))

=======
Suggestion 3

def main():
    a, b, x = map(int, input().split())
    if x <= a**2 * b / 2:
        print(math.degrees(math.atan(2 * x / (a**2 * b))))
    else:
        print(math.degrees(math.atan(2 * (a**2 * b - x) / (a**3))))

=======
Suggestion 4

def main():
    a, b, x = map(int, input().split())
    if x < a**2*b/2:
        print(math.degrees(math.atan(2*x/(a**2*b))))
    else:
        print(math.degrees(math.atan(a*b**2/(2*(a**2*b-x)))))

=======
Suggestion 5

def main():
    a, b, x = map(int, input().split())
    if x < a**2 * b / 2:
        print(math.degrees(math.atan(2 * x / (a**2 * b))))
    else:
        print(math.degrees(math.atan(a * b**2 / (2 * x))))

=======
Suggestion 6

def main():
    a, b, x = map(int, input().split())
    if x < a ** 2 * b / 2:
        print((180 / math.pi) * math.atan(2 * x / (a ** 2)))
    else:
        print((180 / math.pi) * math.atan(2 * (a ** 2 * b - x) / (a ** 3)))

=======
Suggestion 7

def main():
    a, b, x = map(int, input().split())

    if x >= a**2*b/2:
        print(90 - math.degrees(math.atan(2*(a**2*b - x)/(a**3))))
    else:
        print(math.degrees(math.atan(a*b**2/(2*x))))

=======
Suggestion 8

def main():
    a,b,x = map(int,input().split())
    if x <= a**2 * b / 2:
        ans = math.degrees(math.atan(2 * x / (a * b**2)))
    else:
        ans = math.degrees(math.atan(2 * (a**2 * b - x) / (a**3 * b)))
    print(ans)

=======
Suggestion 9

def main():
    a,b,x = map(int, input().split())
    if x > a**2*b/2:
        print(2*(a**2*b-x)/(a**3))
    else:
        print(90-2*x/(a**2))
