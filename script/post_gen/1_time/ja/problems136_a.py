Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, C = map(int, input().split())
    print(max(0, C - (A - B)))

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    print(max(0, c - (a - b)))

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    if a > b:
        if a - b >= c:
            print(0)
        else:
            print(c - (a - b))
    else:
        print(c)

=======
Suggestion 4

def solve():
    A, B, C = map(int, input().split())
    print(max(0, C - (A - B)))

=======
Suggestion 5

def main():
    a,b,c = map(int,input().split())
    print(max(c-(a-b),0))

=======
Suggestion 6

def main():
    a,b,c = map(int,input().split())
    print(c if a >= b + c else b + c - a)

=======
Suggestion 7

def main():
    a,b,c = map(int,input().split())
    print(c if c <= a - b else a - b)
