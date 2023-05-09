Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if a > b:
        print(a - b)
    else:
        print(0)

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    if A < B:
        print(0)
    else:
        print(A-B*2)

=======
Suggestion 3

def main():
    a,b = map(int, input().split())
    if a <= b:
        print(0)
    else:
        print(a-b*2)

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    print(max(0, a - 2 * b))

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    print(a - b * 2 if a > b * 2 else 0)

=======
Suggestion 6

def main():
    A,B = map(int,input().split())
    if A <= B:
        print(0)
    else:
        print(A-2*B)

=======
Suggestion 7

def solve():
    A, B = map(int, input().split())
    print(max(0, A - B * 2))
