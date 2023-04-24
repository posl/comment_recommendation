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
    for i in range(N):
        if S[i] == 'o':
            X += 1
        else:
            if X > 0:
                X -= 1
    print(X)

main()

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
    N, X = map(int, input().split())
    S = input()
    for i in range(N):
        if S[i] == "x":
            if X > 0:
                X -= 1
        else:
            X += 1
    print(X)

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    S = input()
    for c in S:
        if c == 'o':
            X += 1
        elif X > 0:
            X -= 1
    print(X)

=======
Suggestion 6

def main():
    n, x = map(int, input().split())
    s = input()
    for i in range(n):
        if s[i] == "x":
            if x > 0:
                x -= 1
        else:
            x += 1
    print(x)

=======
Suggestion 7

def main():
    N, X = [int(x) for x in input().split()]
    S = input()
    for s in S:
        if s == 'o':
            X += 1
        else:
            X = max(0, X-1)
    print(X)
