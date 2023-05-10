Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, C = map(int, input().split())
    print(max(0, C - (A - B)))

=======
Suggestion 2

def main():
    A, B, C = map(int, input().split())
    print(max(C - (A - B), 0))

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    print(max(0, c - (a - b)))

=======
Suggestion 4

def water_transfer():
    a,b,c = map(int,input().split())
    if a >= b+c:
        print(0)
    else:
        print(c-(a-b))

=======
Suggestion 5

def main():
    a, b, c = map(int, input().split())
    print(0 if a >= b + c else c - (a - b))

=======
Suggestion 6

def solve():
    a, b, c = map(int, input().split())
    ans = max(0, c - (a - b))
    print(ans)
