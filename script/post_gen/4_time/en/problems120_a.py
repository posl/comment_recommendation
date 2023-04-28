Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, C = map(int, input().split())
    if A * C > B:
        print(B // A)
    else:
        print(C)

=======
Suggestion 2

def main():
    A, B, C = input().split()
    A = int(A)
    B = int(B)
    C = int(C)

    if A * C > B:
        print(B // A)
    else:
        print(C)

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    if a * c > b:
        print(b // a)
    else:
        print(c)

=======
Suggestion 4

def main():
    A, B, C = map(int, input().split())
    if A * C <= B:
        print(C)
    else:
        print(B // A)

=======
Suggestion 5

def main():
    A, B, C = map(int, input().split())
    if B // A >= C:
        print(C)
    else:
        print(B // A)

=======
Suggestion 6

def main():
    a, b, c = map(int, input().split())
    print(min(b // a, c))

=======
Suggestion 7

def main():
    A, B, C = map(int, input().split())
    print(min(B//A, C))
