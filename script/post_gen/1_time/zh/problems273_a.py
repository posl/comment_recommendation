Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def f(x):
    if x == 0:
        return 1
    else:
        return x * f(x-1)

n = int(input())
print(f(n))

=======
Suggestion 2

def f(x):
    if x == 0:
        return 1
    else:
        return x * f(x - 1)

N = int(input())
print(f(N))

=======
Suggestion 3

def func(n):
    if n==0:
        return 1
    else:
        return n*func(n-1)
n=int(input())
print(func(n))

=======
Suggestion 4

def f(x):
    if x == 0:
        return 1
    return x * f(x-1)

=======
Suggestion 5

def f(x):
    if x == 0:
        return 1
    else:
        return x * f(x - 1)

=======
Suggestion 6

def f(x):
    if x == 0:
        return 1
    else:
        return x * f(x - 1)

print(f(int(input())))
