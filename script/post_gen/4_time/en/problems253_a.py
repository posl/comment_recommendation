Synthesizing 10/10 solutions (Duplicates hidden)

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
    if b == max(a, b, c) or b == min(a, b, c):
        print('No')
    else:
        print('Yes')

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    if b > a and b < c:
        print('Yes')
    elif b < a and b > c:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    a, b, c = map(int, input().split())
    if b < a:
        a, b = b, a
    if c < b:
        b, c = c, b
    if b == a:
        print("No")
    elif b == c:
        print("No")
    else:
        print("Yes")

=======
Suggestion 5

def median(a,b,c):
    if (a <= b and b <= c) or (c <= b and b <= a):
        return True
    else:
        return False

a,b,c = map(int, input().split())

=======
Suggestion 6

def median(a, b, c):
    if (a<=b and b<=c) or (c<=b and b<=a):
        return True
    else:
        return False

=======
Suggestion 7

def main():
    a, b, c = map(int, input().split())
    if b in [a, c]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def median(a, b, c):
    if b == max(a, b, c) or b == min(a, b, c):
        return False
    return True

=======
Suggestion 9

def main():
    a = input()
    b = input()
    c = input()
    if(b > a and b < c) or (b > c and b < a):
        print("Yes")
    else:
        print("No")
