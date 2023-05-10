Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B = map(int, input().split())

    if A == B:
        print(A*2)
    elif A > B:
        print(A + (A-1))
    else:
        print(B + (B-1))

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if a == b:
        print(a * 2)
    else:
        print(max(a, b) * 2 - 1)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    print(max(a + a - 1, b + b - 1, a + b))

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    print(max(A*2-1, B*2-1, A+B))

=======
Suggestion 5

def main():
    a,b = map(int, input().split())
    print(max(a+b, a+a-1, b+b-1))

=======
Suggestion 6

def main():
    a,b = map(int, input().split())

    if a > b:
        print(a + a - 1)
    elif a < b:
        print(b + b - 1)
    else:
        print(a + b)

=======
Suggestion 7

def main():
    a, b = map(int, input().split())
    if a >= b:
        print(a*2-1)
    else:
        print(b*2-1)

=======
Suggestion 8

def main():
    a, b = map(int, input().split())
    print(max(a+a-1, a+b, b+b-1))

=======
Suggestion 9

def main():
    a, b = map(int, input().split())
    if a > b:
        print(a + (a - 1))
    elif a < b:
        print(b + (b - 1))
    else:
        print(a + b)
