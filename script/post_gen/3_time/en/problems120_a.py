Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, C = map(int, input().split())
    if A * C <= B:
        print(C)
    else:
        print(B // A)

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    if a * c <= b:
        print(c)
    else:
        print(int(b / a))

=======
Suggestion 3

def main():
    A, B, C = map(int, input().split())
    if B // A <= C:
        print(B // A)
    else:
        print(C)

=======
Suggestion 4

def main():
    a, b, c = map(int, input().split())
    print(min(b//a, c))

=======
Suggestion 5

def problems120_a():
    a, b, c = map(int, input().split())
    print(min(b//a, c))

=======
Suggestion 6

def main():
    a, b, c = map(int, input().split())
    print(min(c, b//a))

=======
Suggestion 7

def main():
    a,b,c = map(int, input().split())
    if(b//a < c):
        print(b//a)
    else:
        print(c)
