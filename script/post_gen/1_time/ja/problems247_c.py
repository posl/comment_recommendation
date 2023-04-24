Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def s(n):
    if n == 1:
        return [1]
    else:
        return s(n-1) + [n] + s(n-1)

=======
Suggestion 2

def s(n):
    if n == 1:
        return [1]
    else:
        return s(n-1) + [n] + s(n-1)

n = int(input())
print(*s(n))

=======
Suggestion 3

def S(n):
    if n == 1:
        return [1]
    else:
        return S(n-1) + [n] + S(n-1)

N = int(input())
print(*S(N))

=======
Suggestion 4

def S(n):
    if n == 1:
        return [1]
    else:
        return S(n-1) + [n] + S(n-1)

n = int(input())
print(*S(n))

=======
Suggestion 5

def s(n):
    if n == 1:
        return [1]
    else:
        return s(n-1) + [n] + s(n-1)

N = int(input())
print(*s(N))

=======
Suggestion 6

def f(n):
    if n == 1:
        return [1]
    else:
        return f(n-1) + [n] + f(n-1)

N = int(input())
print(*f(N))

=======
Suggestion 7

def main():
    N = int(input())
    S = [1]
    for i in range(N):
        S = S + [i+2] + S
    print(*S)
