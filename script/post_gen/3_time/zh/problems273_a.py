Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def f(x):
    if x == 0:
        return 1
    else:
        return x * f(x-1)

=======
Suggestion 2

def f(x):
    if x == 0:
        return 1
    else:
        return x * f(x - 1)

n = int(input())
print(f(n))

=======
Suggestion 3

def f(n):
    if n == 0:
        return 1
    else:
        return n * f(n-1)

n = int(input())
print(f(n))

=======
Suggestion 4

def f(n):
    if n == 0:
        return 1
    elif n > 0:
        return n * f(n - 1)

print(f(10))

=======
Suggestion 5

def f(n):
    if n == 0:
        return 1
    else:
        return n * f(n-1)

N = int(input())
print(f(N))
