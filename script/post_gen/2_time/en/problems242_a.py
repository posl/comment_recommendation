Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, C, X = map(int, input().split())
    if X <= A:
        print(1)
    elif X <= B:
        print(C / (B - A + 1))
    else:
        print(0)

=======
Suggestion 2

def main():
    a, b, c, x = map(int, input().split())
    if x <= a:
        print(1)
    elif x > b:
        print(0)
    else:
        print((b - x + 1) / (b - a + 1))

=======
Suggestion 3

def main():
    A, B, C, X = map(int, input().split())
    print((B - X + 1) / (B - A + 1) * C / (B - A + 1 - C))

=======
Suggestion 4

def main():
    A, B, C, X = map(int, input().split())
    if X < A:
        print(0)
    elif X >= A and X <= B:
        print(1/C)
    else:
        print(1)

=======
Suggestion 5

def main():
    A, B, C, X = map(int, input().split())
    print(((C / (B - A + 1)) if A <= X <= B else 0) + (1 if X <= A else 0))

=======
Suggestion 6

def main():
    a, b, c, x = map(int, input().split())
    print((min(x - 1, b - a) - max(0, x - c - a) + 1) / (b - a + 1))

=======
Suggestion 7

def main():
    A, B, C, X = map(int, input().split())
    print((B - A + 1) / (B - A + 1 + C) if A <= X <= B else 0)

=======
Suggestion 8

def main():
    A, B, C, X = map(int, input().split())
    if X >= A:
        if X <= B:
            print(1)
        else:
            print(0)
    else:
        print((C)/(B-A+1))

=======
Suggestion 9

def main():
    A,B,C,X = map(int,input().split())
    if X<=A:
        print(1)
    elif X<=B:
        print(1-C/(B-A))
    else:
        print(0)

=======
Suggestion 10

def main():
    A, B, C, X = map(int, input().split())
    ans = 0
    ans += max(0, X - A + 1) * max(0, B - X + 1)
    ans += max(0, X - A) * max(0, B - X)
    ans -= max(0, X - A) * max(0, B - X) * (C / (B - A + 1))
    ans /= (B - A + 1) * (B - A + 1)
    print(ans)
