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
    A, B, C = map(int, input().split())
    if B//A >= C:
        print(C)
    else:
        print(B//A)

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    if b >= a * c:
        print(c)
    else:
        print(b // a)

=======
Suggestion 4

def main():
    a, b, c = map(int, input().split())
    print(min(b//a, c))

=======
Suggestion 5

def main():
    A, B, C = map(int, input().split())
    print(min(B//A, C))

=======
Suggestion 6

def main():
    A, B, C = map(int, input().split())
    if C < B // A:
        print(C)
    else:
        print(B // A)

=======
Suggestion 7

def main():
    a, b, c = map(int, input().split())
    if a <= b:
        print(c // a)
    else:
        print(b // a)

=======
Suggestion 8

def main():
    A,B,C = map(int,input().split())
    if A <= B:
        if B <= C:
            print(B//A)
        else:
            print(C//A)
    else:
        print(0)
