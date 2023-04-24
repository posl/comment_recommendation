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

def main():
    a, b = map(int, input().split())
    if a < 10 and b < 10:
        print(a * b)
    else:
        print(-1)

=======
Suggestion 4

def main():
    # Read the numbers from the input
    A, B = map(int, input().split())

    # Check if the numbers are between 1 and 9
    if A < 1 or A > 20 or B < 1 or B > 20:
        print(-1)
    else:
        print(A * B)
