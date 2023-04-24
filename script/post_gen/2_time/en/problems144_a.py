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
    if A > 9 or B > 9:
        print(-1)
    else:
        print(A * B)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if a <= 9 and b <= 9:
        print(a*b)
    else:
        print(-1)

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    if a >= 10 or b >= 10:
        print(-1)
    else:
        print(a * b)

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    if (a >= 1 and a <= 20) and (b >= 1 and b <= 20):
        if a * b <= 20:
            print(a * b)
        else:
            print(-1)
    else:
        print(-1)
