Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def f(x):
    if x == 0:
        return 1
    else:
        return x * f(x-1)

N = int(input())
print(f(N))

=======
Suggestion 2

def f(x):
    if x == 0:
        return 1
    else:
        return x * f(x-1)

n = int(input())
print(f(n))

=======
Suggestion 3

def f(x):
    return x * f(x-1) if x > 0 else 1

n = int(input())
print(f(n))

=======
Suggestion 4

def f(n):
    if n == 0:
        return 1
    else:
        return n * f(n-1)

=======
Suggestion 5

def f(x):
    if x == 0:
        return 1
    else:
        return x * f(x-1)

print(f(int(input())))

=======
Suggestion 6

def f(n):
    if n == 0:
        return 1
    else:
        return n * f(n - 1)

N = int(input())
print(f(N))

=======
Suggestion 7

def f(n):
    if n == 0:
        return 1
    else:
        return n * f(n-1)

n = int(input())
print(f(n))

=======
Suggestion 8

def main():
    n = int(input())
    if n == 0:
        print(1)
    else:
        print(n*main())
