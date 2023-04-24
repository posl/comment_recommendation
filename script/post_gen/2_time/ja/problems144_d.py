Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, x = map(int, input().split())
    if x <= a * a * b / 2:
        print(math.degrees(math.atan(2 * x / (a * a * b))))
    else:
        print(math.degrees(math.atan(a * b * b / (2 * x))))

=======
Suggestion 2

def main():
    a, b, x = map(int, input().split())
    if x <= a * a * b / 2:
        print(math.degrees(math.atan(2 * x / (a * a * b))))
    else:
        print(math.degrees(math.atan(2 * (a * a * b - x) / (a * a * a))))

=======
Suggestion 3

def main():
    a, b, x = map(int, input().split())
    if a * a * b / 2 > x:
        print(math.degrees(math.atan(2 * (a * a * b - x) / (a * a * a))))
    else:
        print(math.degrees(math.atan((a * b * b) / (2 * (a * a * b - x)))))

=======
Suggestion 4

def main():
    a, b, x = map(int, input().split())
    if a ** 2 * b / 2 >= x:
        print(math.degrees(math.atan(2 * x / a ** 3)))
    else:
        print(math.degrees(math.atan(a ** 2 / (2 * x / a ** 2 - b))))

=======
Suggestion 5

def main():
    a, b, x = map(int, input().split())
    if a ** 2 * b / 2 < x:
        print(90 - math.degrees(math.atan(2 * (a ** 2 * b - x) / (a ** 3))))
    else:
        print(math.degrees(math.atan(a * b ** 2 / (2 * x))))

=======
Suggestion 6

def main():
    a, b, x = map(int, input().split())
    if x <= a**2*b/2:
        ans = math.degrees(math.atan(2*x/(a**3)))
    else:
        ans = math.degrees(math.atan((2*a**2*b-2*x)/(a**3)))
    print(ans)

=======
Suggestion 7

def main():
    a,b,x = map(int,input().split())
    if x <= a**2*b/2:
        print(math.degrees(math.atan(2*x/(a**2*b))))
    else:
        print(math.degrees(math.atan(2*(a**2*b-x)/(a**3))))

=======
Suggestion 8

def main():
    a, b, x = map(int, input().split())
    if x >= a * a * b / 2:
        print(90 - math.atan(2 * (a * a * b - x) / a ** 3) * 180 / math.pi)
    else:
        print(math.atan(a * b * b / 2 / x) * 180 / math.pi)

=======
Suggestion 9

def main():
    a, b, x = map(int, input().split())
    if x >= a**2 * b / 2:
        print(90 - math.degrees(math.atan(2*(a**2*b - x)/(a**3))))
    else:
        print(math.degrees(math.atan(a*b**2/(2*x))))

=======
Suggestion 10

def main():
    # 入力
    a,b,x = map(int,input().split())

    # 処理
    if x >= a**2*b/2:
        ans = math.degrees(math.atan(2*(a**2*b-x)/(a**3)))
    else:
        ans = math.degrees(math.atan(a*b**2/(2*x)))
    # 出力
    print(ans)
