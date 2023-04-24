Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if 1 <= a <= 9 and 1 <= b <= 9:
        print(a * b)
    else:
        print(-1)

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if a >= 1 and a <= 9 and b >= 1 and b <= 9:
        print(a * b)
    else:
        print(-1)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if a <= 9 and b <= 9:
        print(a * b)
    else:
        print(-1)

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    if A <= 9 and B <= 9:
        print(A * B)
    else:
        print(-1)

=======
Suggestion 5

def main():
    A, B = map(int, input().split())

    if A > 9 or B > 9:
        print(-1)
    else:
        print(A * B)
