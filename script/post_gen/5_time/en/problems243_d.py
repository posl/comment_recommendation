Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    S = input()
    for s in S:
        if s == 'L':
            X = X * 2
        elif s == 'R':
            X = X * 2 + 1
        else:
            X = (X - 1) // 2
    print(X)

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    s = input()
    for i in range(n):
        if s[i] == 'L':
            x = x * 2
        elif s[i] == 'R':
            x = x * 2 + 2
        else:
            x = x * 2 + 1
    print(x)

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    S = input()
    for i in range(N):
        if S[i] == 'U':
            X //= 2
        elif S[i] == 'L':
            X = 2*X - 1
        else:
            X = 2*X + 1
    print(X)

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    s = input()
    for i in range(n):
        if s[i] == 'L':
            x = 2*x
        elif s[i] == 'R':
            x = 2*x+1
        else:
            x = (x-1)//2
    print(x)

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    S = input()
    for s in S:
        if s == "U":
            X = X // 2
        elif s == "L":
            X = X * 2
        else:
            X = X * 2 + 1
    print(X)

=======
Suggestion 6

def solve():
    N, X = map(int, input().split())
    S = input()
    for s in S:
        if s == 'U':
            X = X // 2
        elif s == 'L':
            X = 2 * X - 1
        else:
            X = 2 * X + 1
    print(X)

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    S = input()
    i = 0
    while i < N:
        if S[i] == 'U':
            X = X // 2
        elif S[i] == 'L':
            X = X * 2
        else:
            X = X * 2 + 1
        i += 1
    print(X)

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    S = input()
    #print(N, X, S)
    ans = X
    for i in range(N):
        if S[i] == 'L':
            ans = ans * 2 - 1
        elif S[i] == 'R':
            ans = ans * 2 + 1
        else:
            ans = ans // 2
    print(ans)

=======
Suggestion 9

def findVertex(N, X, S):
    for i in range(N):
        if S[i] == 'U':
            X = X // 2
        elif S[i] == 'L':
            X = X * 2 - 1
        else:
            X = X * 2 + 1
    return X

=======
Suggestion 10

def get_path(n):
    path = []
    while n > 1:
        path.append(n)
        n //= 2
    return path
