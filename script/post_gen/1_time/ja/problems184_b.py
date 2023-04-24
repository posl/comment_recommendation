Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    S = input()
    for i in range(N):
        if S[i] == "o":
            X += 1
        else:
            if X > 0:
                X -= 1
    print(X)

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    S = input()
    for s in S:
        if s == "o":
            X += 1
        else:
            if X > 0:
                X -= 1
    print(X)

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    S = input()
    for i in range(N):
        if S[i] == 'o':
            X += 1
        else:
            X -= 1
            if X < 0:
                X = 0
    print(X)

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    S = input()
    for i in range(N):
        if S[i] == 'o':
            X += 1
        elif X > 0:
            X -= 1
    print(X)

=======
Suggestion 5

def main():
    n, x = map(int, input().split())
    s = input()
    for i in range(n):
        if s[i] == "o":
            x += 1
        elif s[i] == "x" and x > 0:
            x -= 1
    print(x)

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    S = input()
    for i in range(N):
        if S[i] == "o":
            X += 1
        elif X != 0:
            X -= 1
    print(X)

=======
Suggestion 7

def quiz(N,X,S):
    for i in range(N):
        if S[i] == 'x' and X > 0:
            X -= 1
        elif S[i] == 'o' and X < 200000:
            X += 1
    return X
