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
    if a <= b <= c or c <= b <= a:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    if b == max(a, b, c) or b == min(a, b, c):
        print("No")
    else:
        print("Yes")

=======
Suggestion 4

def main():
    a, b, c = map(int, input().split())
    if a < b < c or c < b < a:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    a,b,c = map(int,input().split())
    if (a<=b and b<=c) or (c<=b and b<=a):
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def median(a,b,c):
    if a < b:
        if b < c:
            return True
        else:
            return False
    else:
        if b > c:
            return True
        else:
            return False

a,b,c = map(int, input().split())

=======
Suggestion 7

def main():
    a,b,c = map(int,input().split())
    if a <= b and b <= c or c <= b and b <= a:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    a,b,c = map(int, input().split())
    if (a < b < c) or (c < b < a):
        print("Yes")
    else:
        print("No")
