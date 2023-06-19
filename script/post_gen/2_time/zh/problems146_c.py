Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def d(n):
    if n < 10:
        return 1
    else:
        return 1 + d(n // 10)

A, B, X = map(int, input().split())

=======
Suggestion 2

def d(n):
    if n < 10:
        return 1
    else:
        return 1 + d(n//10)

=======
Suggestion 3

def d(x):
    if x < 10:
        return 1
    else:
        return 1 + d(x // 10)

=======
Suggestion 4

def d(N):
    if N < 10:
        return 1
    else:
        return d(int(N/10)) + 1

A,B,X = map(int,input().split())

=======
Suggestion 5

def d(N):
    return len(str(N))

=======
Suggestion 6

def d(n):
    if n < 10:
        return 1
    return d(n//10) + 1

=======
Suggestion 7

def d(n):
    return len(str(n))

=======
Suggestion 8

def d(n):
    if n < 10:
        return 1
    else:
        return d(n // 10) + 1
