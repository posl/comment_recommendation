Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    if a * c <= b:
        print(c)
    else:
        print(b // a)

=======
Suggestion 2

def main():
    A, B, C = map(int, input().split())
    if A * C <= B:
        print(C)
    else:
        print(B // A)

=======
Suggestion 3

def solve():
    a, b, c = map(int, input().split())
    if a * c <= b:
        print(c)
    else:
        print(b // a)

=======
Suggestion 4

def solve():
    a, b, c = map(int, input().split())
    if b >= a * c:
        print(c)
    else:
        print(b // a)

=======
Suggestion 5

def main():
    a, b, c = map(int, input().split())
    print(min(b//a, c))

=======
Suggestion 6

def main():
    a,b,c = map(int,input().split())
    if b >= a*c:
        print(c)
    else:
        print(b//a)
