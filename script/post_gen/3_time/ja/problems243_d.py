Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    S = input()
    for i in range(N):
        if S[i] == "U":
            X = X // 2
        elif S[i] == "L":
            X = 2 * X - 1
        else:
            X = 2 * X + 1
    print(X)

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    S = input()
    for i in range(N):
        if S[i] == "U":
            X = (X + 1) // 2
        elif S[i] == "L":
            X *= 2
        elif S[i] == "R":
            X = X * 2 + 1
        else:
            print("error")
    print(X)

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    S = input()

    for i in range(N):
        if S[i] == "U":
            X //= 2
        elif S[i] == "L":
            X = (X-1)//2
        elif S[i] == "R":
            X = (X-1)//2 + 1

    print(X)

=======
Suggestion 4

def main():
    N,X = map(int,input().split())
    S = input()
    for i in range(N):
        if S[i] == "U":
            X = (X-1)//2
        elif S[i] == "L":
            X = 2*X
        elif S[i] == "R":
            X = 2*X+1
    print(X)

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    S = input()
    for i in range(N):
        if S[i] == 'U':
            X = (X+1)//2
        elif S[i] == 'L':
            X = X*2
        elif S[i] == 'R':
            X = X*2+1
    print(X)

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    S = input()
    for i in range(N):
        if S[i] == 'U':
            X = (X-1)//2
        elif S[i] == 'L':
            X = 2*X
        else:
            X = 2*X+1
    print(X)

=======
Suggestion 7

def main():
    n, x = map(int, input().split())
    s = input()
    for i in range(n):
        if s[i] == 'U':
            if x % 2 == 0:
                x = x // 2
            else:
                x = (x - 1) // 2
        elif s[i] == 'L':
            x = 2 * x - 1
        else:
            x = 2 * x + 1
    print(x)

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    S = input()
    for s in S:
        if s == "U":
            if X % 2 == 0:
                X = X // 2
        elif s == "L":
            X = X * 2
        elif s == "R":
            X = X * 2 + 1
    print(X)

=======
Suggestion 9

def main():
    N,X = map(int,input().split())
    S = input()
    for i in range(N):
        if S[i] == "U":
            if X%2 == 0:
                X //= 2
            else:
                X = (X-1)//2
        elif S[i] == "L":
            X = 2*X-1
        else:
            X = 2*X
    print(X)

=======
Suggestion 10

def main():
    N,X = map(int, input().split())
    S = input()
    for s in S:
        if s == "U":
            X = (X-1)//2
        elif s == "L":
            X = 2*X
        else:
            X = 2*X+1
    print(X)
