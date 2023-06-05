Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a,b,c = map(int,input().split())
    if a <= b <= c or c <= b <= a:
        print("是")
    else:
        print("否")

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    if b in [a, c]:
        print("没有")
    else:
        print("是")

=======
Suggestion 3

def is_middle(a, b, c):
    if (a <= b and b <= c) or (c <= b and b <= a):
        return True
    else:
        return False

=======
Suggestion 4

def main():
    a, b, c = map(int, input().split())
    if a <= b <= c or c <= b <= a:
        print('是')
    else:
        print('没有')

=======
Suggestion 5

def main():
    a,b,c = map(int,input().split())
    if a <= b <= c or c <= b <= a:
        print('是')
    else:
        print('否')

=======
Suggestion 6

def main():
    a, b, c = map(int, input().split())
    if a < b < c or c < b < a:
        print("是")
    else:
        print("没有")

=======
Suggestion 7

def main():
    a, b, c = map(int, input().split())
    if b > a and b < c or b < a and b > c:
        print("是")
    else:
        print("否")

=======
Suggestion 8

def main():
    a,b,c = map(int,input().split())
    if a<=b<=c or c<=b<=a:
        print("是")
    else:
        print("没有")

=======
Suggestion 9

def main():
    a,b,c = map(int,input().split())
    if b in [a,c]:
        print('是')
    else:
        print('没有')

=======
Suggestion 10

def main():
    a,b,c = map(int,input().split())
    if b == max(a,b,c) or b == min(a,b,c):
        print("没有")
    else:
        print("是")
