Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    print(max(a + b, b + c, c + a))

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    print(max(a+b, a+c, b+c))

=======
Suggestion 3

def main():
    # input
    a, b, c = map(int, input().split())

    # compute

    # output
    print(max(a+b, b+c, c+a))

=======
Suggestion 4

def main():
    A, B, C = map(int, input().split())
    print(max(A+B, B+C, C+A))

=======
Suggestion 5

def solve():
    # Implement solution here
    a,b,c = map(int,input().split())
    print(a+b+c-max(a,b,c))
