Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    a,b,c = map(int,input().split())
    if a*c <= b:
        print(c)
    else:
        print(b//a)

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    if b // a >= c:
        print(c)
    else:
        print(b // a)

=======
Suggestion 3

def main():
    a,b,c = map(int,input().split())
    if a*c <= b:
        print(c)
    else:
        print(b//a)

=======
Suggestion 4

def main():
    a,b,c = map(int, input().split())
    if a*c <= b:
        print(c)
    else:
        print(int(b/a))

=======
Suggestion 5

def main():
    a, b, c = map(int, input().split())
    if b >= a * c:
        print(c)
    else:
        print(b // a)

=======
Suggestion 6

def main():
    A, B, C = map(int, input().split())
    if A * C <= B:
        print(C)
    else:
        print(B // A)

=======
Suggestion 7

def calc():
    a, b, c = map(int, input().split())
    if a * c > b:
        return b // a
    else:
        return c

print(calc())
