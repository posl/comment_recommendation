Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b,c = map(int,input().split())
    print(max(a+b,b+c,c+a))

=======
Suggestion 2

def main():
    # input
    a, b, c = map(int, input().split())

    # compute

    # output
    print(max(a+b, b+c, c+a))

=======
Suggestion 3

def solve():
    a,b,c = map(int, input().split())
    print(a+b+c-max(a,b,c))

=======
Suggestion 4

def main():
    a, b, c = map(int, input().split())
    print(a + b + c - min(a, b, c))

=======
Suggestion 5

def main():
    a,b,c = map(int, input().split())
    print(a+b+c-max(a,b,c))

=======
Suggestion 6

def main():
    # input
    A, B, C = map(int, input().split())

    # compute
    ans = max(A+B, B+C, C+A)

    # output
    print(ans)

=======
Suggestion 7

def main():
    cards = [int(x) for x in input().split()]
    print(sum(cards) - min(cards))

=======
Suggestion 8

def main():
    A, B, C = map(int, input().split())
    print(A+B+C-max(A,B,C))
