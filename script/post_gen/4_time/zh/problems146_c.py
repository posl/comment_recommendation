Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def d(n):
    if n < 10:
        return 1
    else:
        return d(n//10) + 1

=======
Suggestion 2

def d(n):
    if n < 10:
        return 1
    return 1 + d(n//10)

=======
Suggestion 3

def main():
    A, B, X = map(int, input().split())
    N = 0
    while True:
        if A * N + B * len(str(N)) > X:
            break
        N += 1
    print(N - 1)

=======
Suggestion 4

def d(n):
    return len(str(n))

=======
Suggestion 5

def d(n):
    if n < 10:
        return n
    else:
        return d(n//10)

=======
Suggestion 6

def d(n):
    if n < 10:
        return 1
    else:
        return d(n // 10) + 1

A, B, X = map(int, input().split())

=======
Suggestion 7

def d(n):
    if n < 10:
        return 1
    else:
        return 1 + d(n//10)

=======
Suggestion 8

def main():
    A, B, X = map(int, input().split())
    l = 0
    r = 10**9 + 1
    while r - l > 1:
        c = (l + r) // 2
        if A * c + B * len(str(c)) <= X:
            l = c
        else:
            r = c
    print(l)
