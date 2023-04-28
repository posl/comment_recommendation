Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    print(c - (a - b) if c - (a - b) > 0 else 0)

=======
Suggestion 2

def main():
    A, B, C = map(int, input().split())
    print(max(0, C - (A - B)))

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    print(max(0, c - (a - b)))

=======
Suggestion 4

def main():
    a, b, c = map(int, input().split())
    print(max(c - (a - b), 0))

=======
Suggestion 5

def main():
    a, b, c = map(int, input().split())
    print(c if a >= b + c else b + c - a)

=======
Suggestion 6

def solve():
    a, b, c = map(int, input().split())
    print(max(0, c-(a-b)))

=======
Suggestion 7

def main():
    A, B, C = map(int, input().rstrip().split())
    print(max(C - (A - B), 0))

=======
Suggestion 8

def solve():
    A,B,C = map(int,input().split())
    if A-B >= C:
        print(0)
    else:
        print(C-(A-B))
