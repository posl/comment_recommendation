Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def d(n):
    return len(str(n))

=======
Suggestion 2

def d(n):
    if n < 10:
        return 1
    else:
        return 1 + d(n//10)

=======
Suggestion 3

def d(N):
    if N < 10:
        return 1
    else:
        return 1 + d(N // 10)

=======
Suggestion 4

def d(n):
    if n == 0:
        return 0
    else:
        return n % 10 + d(n // 10)

=======
Suggestion 5

def d(N):
    if N < 10:
        return 1
    else:
        return d(N//10) + 1

=======
Suggestion 6

def d(n):
    if n < 10:
        return n
    else:
        return d(n // 10)

A, B, X = map(int, input().split())
