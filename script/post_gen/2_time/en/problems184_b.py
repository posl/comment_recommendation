Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    S = input()
    for i in range(N):
        if S[i] == 'o':
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
        if s == 'o':
            X += 1
        else:
            if X > 0:
                X -= 1
    print(X)

=======
Suggestion 3

def main():
    n, x = map(int, input().split())
    s = input()
    for i in range(n):
        if s[i] == 'o':
            x += 1
        else:
            if x > 0:
                x -= 1
    print(x)

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    s = input()
    for i in range(n):
        if s[i] == 'o':
            x += 1
        elif s[i] == 'x' and x > 0:
            x -= 1
    print(x)

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    S = input()
    for i in range(N):
        if S[i] == 'x':
            if X > 0:
                X -= 1
        else:
            X += 1
    print(X)

=======
Suggestion 6

def answer(N, X, S):
    points = X
    for i in range(N):
        if S[i] == 'o':
            points += 1
        else:
            if points > 0:
                points -= 1
    return points

=======
Suggestion 7

def main():
    # Take input
    N, X = map(int, input().split())
    S = input()

    # Solve problem
    for i in range(N):
        if S[i] == 'o':
            X += 1
        else:
            if X > 0:
                X -= 1
    # Output result
    print(X)
