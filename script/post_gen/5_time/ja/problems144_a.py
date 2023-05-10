Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if a > 9 or b > 9:
        print(-1)
    else:
        print(a*b)

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    if A <= 9 and B <= 9:
        print(A*B)
    else:
        print(-1)

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    if 0 < A <= 20 and 0 < B <= 20:
        print(A * B if A * B <= 20 else -1)
    else:
        print(-1)

=======
Suggestion 4

def calc(a, b):
    if a >= 1 and a <= 20 and b >= 1 and b <= 20:
        return a * b
    else:
        return -1

=======
Suggestion 5

def calc(a, b):
    if a > 9 or b > 9:
        return -1
    else:
        return a * b
