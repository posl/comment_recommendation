Synthesizing 10/10 solutions

=======
Suggestion 1

def median(a,b,c):
    if a < b:
        if b < c:
            return b
        elif a < c:
            return c
        else:
            return a
    else:
        if a < c:
            return a
        elif b < c:
            return c
        else:
            return b

=======
Suggestion 2

def median(a,b,c):
    if ((a>b and a<c) or (a>c and a<b)):
        return True
    else:
        return False

=======
Suggestion 3

def sort(a, b, c):
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b

    return a, b, c

=======
Suggestion 4

def is_middle(a,b,c):
    if a<b<c or c<b<a:
        return True
    else:
        return False

=======
Suggestion 5

def main():
    a, b, c = map(int, input().split())
    if a <= b <= c or c <= b <= a:
        print('是')
    else:
        print('没有')

=======
Suggestion 6

def main():
    a,b,c = map(int, input().split())
    if b == a or b == c:
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
        print("没有")

=======
Suggestion 8

def median(a, b, c):
    if a < b:
        if b < c:
            return b
        else:
            if a < c:
                return c
            else:
                return a
    else:
        if a < c:
            return a
        else:
            if b < c:
                return c
            else:
                return b

a, b, c = map(int, input().split())

print('是' if b == median(a, b, c) else '否')

=======
Suggestion 9

def main():
    a,b,c = map(int,input().split())
    if b>a and b<c or b<a and b>c:
        print('是')
    else:
        print('没有')

=======
Suggestion 10

def main():
    a,b,c = map(int,input().split())
    if b == sorted([a,b,c])[1]:
        print("是")
    else:
        print("没有")
