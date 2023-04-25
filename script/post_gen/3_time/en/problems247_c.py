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

n = int(input())
print(*S(n))

=======
Suggestion 4

def S(n):
    if n == 1:
        return [1]
    else:
        return S(n-1) + [n] + S(n-1)

N = int(input())
print(*S(N))

=======
Suggestion 5

def s(n):
    if n == 1:
        return [1]
    else:
        return s(n - 1) + [n] + s(n - 1)

print(*s(int(input())))

=======
Suggestion 6

def seq(n):
    if n == 1:
        return [1]
    else:
        return seq(n-1) + [n] + seq(n-1)

n = int(input())
for i in seq(n):
    print(i, end=' ')

=======
Suggestion 7

def f(n):
    if n == 1:
        return [1]
    else:
        return f(n - 1) + [n] + f(n - 1)

=======
Suggestion 8

def S(n):
    if n == 1:
        return [1]
    else:
        return S(n-1) + [n] + S(n-1)

N = int(input())
print(' '.join(map(str,S(N))))

=======
Suggestion 9

def make_seq(n):
    if n == 1:
        return [1]
    else:
        return make_seq(n-1) + [n] + make_seq(n-1)

N = int(input())
print(*make_seq(N))
