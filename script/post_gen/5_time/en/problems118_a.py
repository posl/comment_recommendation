Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if b % a == 0:
        print(a + b)
    else:
        print(b - a)

=======
Suggestion 2

def main():
    A, B = map(int, input().split())

    if B % A == 0:
        print(A + B)
    else:
        print(B - A)
