Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, C, X = map(int, input().split())
    if X <= A:
        print(1)
    elif A < X <= A + C:
        print((C + 1) / (B - A + 1))
    else:
        print(0)

=======
Suggestion 2

def main():
    a, b, c, x = map(int, input().split())
    if a < x <= b:
        print(c / (b - a))
    elif x <= a:
        print(1)
    else:
        print(0)

=======
Suggestion 3

def main():
    A, B, C, X = map(int, input().split())
    if X <= A:
        print(1)
    elif A < X <= B:
        print(1 - C / (B - A))
    else:
        print(0)

=======
Suggestion 4

def main():
    A, B, C, X = map(int, input().split())
    ans = 0
    for i in range(A):
        ans += 1
    for i in range(A, B):
        ans += C/(B-A)
    for i in range(B, X):
        ans += 0
    print(ans)

=======
Suggestion 5

def main():
    A,B,C,X = map(int,input().split())
    ans = 0
    for i in range(A):
        ans += 1
    for i in range(A,B):
        ans += 1/470
    for i in range(C):
        ans += 1/470
    print(ans)

=======
Suggestion 6

def main():
    A, B, C, X = map(int, input().split())
    print((1 - ((B - X) / (B - A)) * ((C - 1) / (B - A))) if A <= X <= B else 0)

=======
Suggestion 7

def main():
    A, B, C, X = map(int, input().split())
    print((A <= X and X <= A + C) / (B - A))

=======
Suggestion 8

def main():
    A, B, C, X = map(int, input().split())
    print(1-(B-X)/(B-A)*((B-A-C)/(B-A)))
