Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    if (b >= a and b <= c) or (b >= c and b <= a):
        print("是")
    else:
        print("否")

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    if ((a <= b and b <= c) or (c <= b and b <= a)):
        print('是')
    else:
        print('没有')

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    if a <= b <= c or c <= b <= a:
        print('是')
    else:
        print('否')

=======
Suggestion 4

def is_middle(a,b,c):
    if b < a:
        if b > c:
            return True
    if b > a:
        if b < c:
            return True
    return False

=======
Suggestion 5

def median(a,b,c):
    if (b>=a and b<=c) or (b<=a and b>=c):
        return True
    else:
        return False

=======
Suggestion 6

def main():
    a,b,c = map(int,input().split())
    if a < b and b < c:
        print("はい")
    else:
        print("いいえ")

=======
Suggestion 7

def main():
    a,b,c = map(int, input().split())
    if (a <= b and b <= c) or (c <= b and b <= a):
        print("是")
    else:
        print("否")

=======
Suggestion 8

def is_median(a,b,c):
    if a<b<c or c<b<a:
        return True
    else:
        return False

=======
Suggestion 9

def main():
    a,b,c = map(int,input().split())
    if b >= min(a,c) and b <= max(a,c):
        print('是')
    else:
        print('没有')

=======
Suggestion 10

def median(a,b,c):
    if b>=a and b<=c:
        return True
    elif b<=a and b>=c:
        return True
    else:
        return False

a,b,c = map(int,input().split())
