Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    if B % A == 0:
        print(A + B)
    else:
        print(B - A)

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if b % a == 0:
        print(a + b)
    else:
        print(b - a)

=======
Suggestion 3

def main():
    # Read the input
    A, B = map(int, input().split())
    # Check if A is a divisor of B
    if B % A == 0:
        # If A is a divisor of B, print A + B
        print(A + B)
    else:
        # If A is not a divisor of B, print B - A
        print(B - A)
