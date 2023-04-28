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
        print(a*b)
    else:
        print(-1)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if (1 <= a and a <= 20) and (1 <= b and b <= 20):
        print(a*b)
    else:
        print(-1)

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    if (1 <= a <= 20) and (1 <= b <= 20):
        print(a*b)
    else:
        print(-1)

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    if a < 1 or a > 20 or b < 1 or b > 20:
        print(-1)
    else:
        print(a*b)

=======
Suggestion 6

def problem():
    a, b = map(int, input().split())
    if 1 <= a <= 20 and 1 <= b <= 20:
        print(a * b if a * b <= 20 else -1)
    else:
        pass

=======
Suggestion 7

def main():
    # Take input
    a, b = map(int, input().split())

    # Calculate and print result
    if 1 <= a <= 9 and 1 <= b <= 9:
        print(a * b)
    else:
        print(-1)
