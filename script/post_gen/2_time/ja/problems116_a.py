Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    AB, BC, CA = map(int, input().split())
    print(int(AB * BC / 2))

=======
Suggestion 2

def main():
    s = input().split()
    a = int(s[0])
    b = int(s[1])
    c = int(s[2])
    print(int(a * b / 2))

=======
Suggestion 3

def main():
    # 標準入力から a, b, c を取得する
    a, b, c = map(int, input().split())
    # 三角形の面積を出力する
    print(int(a * b / 2))

=======
Suggestion 4

def main():
    a, b, c = map(int, input().split())
    print(int(a*b/2))

=======
Suggestion 5

def main():
    num = input().split()
    a = int(num[0])
    b = int(num[1])
    c = int(num[2])
    print(int(a*b/2))

=======
Suggestion 6

def main():
    a, b, c = map(int, input().split())
    print((a*b)//2)

=======
Suggestion 7

def area():
    a = [int(x) for x in input().split()]
    print(a[0] * a[1] // 2)

area()

=======
Suggestion 8

def area_of_right_triangle(a, b):
    return a * b / 2
