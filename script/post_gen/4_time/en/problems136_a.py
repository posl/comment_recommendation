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
        print(c - (a - b))
    else:
        print(c)

=======
Suggestion 4

def main():
    a, b, c = map(int, input().split())
    print(c if a >= b+c else c-(a-b))

=======
Suggestion 5

def problem136_a():
    a,b,c = map(int,input().split())
    print(min(c,a-b))
