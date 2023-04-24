Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, C = map(int, input().split())
    if B + C <= A:
        print(0)
    else:
        print(B + C - A)

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    print(c - (a - b) if c - (a - b) > 0 else 0)

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    print(max(0, c - (a - b)))

=======
Suggestion 4

def main():
    A, B, C = map(int, input().split())
    print(max(C - (A - B), 0))

=======
Suggestion 5

def main():
    A, B, C = map(int, input().split())
    if A-B >= C:
        print(C)
    else:
        print(A-B)

=======
Suggestion 6

def main():
    # Write your code here
    A, B, C = map(int, input().split())
    if A-B >= C:
        print(C)
    else:
        print(A-B)

=======
Suggestion 7

def main():
    A,B,C = map(int, input().split())
    print(max(0,C-(A-B)))
