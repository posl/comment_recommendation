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
    a, b = map(int, input().split())
    if a <= 9 and b <= 9:
        print(a * b)
    else:
        print(-1)

=======
Suggestion 3

def calc(a, b):
    if 1 <= a <= 20 and 1 <= b <= 20:
        return a * b
    else:
        return -1

a, b = map(int, input().split())
print(calc(a, b))

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    if (A > 9) or (B > 9):
        print(-1)
    else:
        print(A * B)

=======
Suggestion 5

def calc(a, b):
    if a > 9 or b > 9:
        return -1
    else:
        return a*b

=======
Suggestion 6

def main():
    A, B = map(int, input().split())
    if A < 1 or A > 20 or B < 1 or B > 20:
        return
    print(A*B) if A <= 9 and B <= 9 else print(-1)

=======
Suggestion 7

def calc(a,b):
    if a <= 9 and b <= 9:
        return a * b
    else:
        return -1
