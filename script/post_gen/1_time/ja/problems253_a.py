Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    if a <= b <= c or c <= b <= a:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    if a <= b <= c or c <= b <= a:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    if b < a:
        a, b = b, a
    if c < a:
        a, c = c, a
    if c < b:
        b, c = c, b
    if b == a or b == c:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    a, b, c = map(int, input().split())
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
    if b == c:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    a, b, c = map(int, input().split())
    if (a < b < c) or (c < b < a):
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    a, b, c = map(int, input().split())
    if b == min(a, b, c) or b == max(a, b, c):
        print('No')
    else:
        print('Yes')

=======
Suggestion 7

def main():
    a, b, c = map(int, input().split())
    if b >= a and b <= c or b <= a and b >= c:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    a,b,c = map(int, input().split())
    if (a <= b <= c) or (c <= b <= a):
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    a, b, c = map(int, input().split())
    print('Yes' if (a <= b and b <= c) or (c <= b and b <= a) else 'No')

=======
Suggestion 10

def main():
    #入力
    a, b, c = map(int, input().split())
    #中央値の判定
    if (a <= b <= c) or (c <= b <= a):
        print("Yes")
    else:
        print("No")
