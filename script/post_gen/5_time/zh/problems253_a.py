Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a = input("输入a: ")
    b = input("输入b: ")
    c = input("输入c: ")
    if (a<=b and

=======
Suggestion 2

def median(a,b,c):
    if a<=b<=c or c<=b<=a:
        return True
    else:
        return False

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    if (a <= b and b <= c) or (c <= b and b <

=======
Suggestion 4

def median(a, b, c):
    if a <= b <= c or c <= b <= a:
        return True
    else:
        ret

=======
Suggestion 5

def main():
    a,b,c = map(int,input().split(" "))
    if a <= b <= c or c <= b <= a:
        print

=======
Suggestion 6

def main():
    a,b,c = map(int, input().split())
    if a <= b <= c or c <= b <= a:
        prin

=======
Suggestion 7

def problems253_a():
    a,b,c = map(int, input().split())
    if (b >= a and b <= c) or (b <= a

=======
Suggestion 8

def main():
    a = input("Please input a:")
    b = input("Please input b:")
    c = input("Please input

=======
Suggestion 9

def main():
    a,b,c = map(int,input().split())
    if a<=b<=c or c<=b<=a:
        print("Yes")

=======
Suggestion 10

def median(a, b, c):
    if a < b:
        if b < c:
            return b
        elif c < a:
