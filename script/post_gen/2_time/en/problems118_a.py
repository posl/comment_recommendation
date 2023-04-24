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
    A, B = input().split()
    A = int(A)
    B = int(B)
    if B % A == 0:
        print(A + B)
    else:
        print(B - A)

=======
Suggestion 4

def main():
    A, B = [int(x) for x in input().split()]
    if B % A == 0:
        print(A + B)
    else:
        print(B - A)

=======
Suggestion 5

def addOrSubtract(a, b):
    if b % a == 0:
        return a + b
    else:
        return b - a

a, b = map(int, input().split())
print(addOrSubtract(a, b))
