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
    a, b, c = map(int, input().split())
    if b >= c * a:
        print(c)
    else:
        print(b // a)

=======
Suggestion 3

def solve():
    a,b,c = map(int,input().split())
    if a*c <= b:
        print(c)
    else:
        print(b//a)

=======
Suggestion 4

def solve(a,b,c):
    if a*c <= b:
        return c
    else:
        return b//a

a,b,c = map(int,input().split())
print(solve(a,b,c))

=======
Suggestion 5

def main():
    a,b,c = map(int, input().split())
    if c * a <= b:
        print(c)
    else:
        print(b // a)

=======
Suggestion 6

def main():
    A, B, C = list(map(int, input().split()))
    if B // A > C:
        print(C)
    else:
        print(B // A)

=======
Suggestion 7

def main():
    A,B,C = map(int,input().split())
    print(min(B//A,C))
