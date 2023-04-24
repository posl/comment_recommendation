Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    print(max(a + b, a + a - 1, b + b - 1))

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    print(max(A + B, A + A - 1, B + B - 1))

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if a > b:
        print(a + b - 1)
    else:
        print(a + b)

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    print(max(A+B, A+B-1, A+B-2))

=======
Suggestion 5

def main():
    a, b = [int(x) for x in input().split()]
    print(max(a+b, a+a-1, b+b-1))

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    print(a + b - 1)

=======
Suggestion 7

def main():
    A,B = map(int,input().split())
    print(max(A+B,A+B-1,A-1+B-1))
