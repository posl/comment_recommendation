Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def f(x):
    if x == 0:
        return 1
    return x * f(x - 1)

n = int(input())
print(f(n))

=======
Suggestion 2

def f(x):
    if x == 0:
        return 1
    else:
        return x*f(x-1)
    
print(f(int(input())))

=======
Suggestion 3

def f(k):
    if k == 0:
        return 1
    else:
        return k * f(k-1)

n = int(input())
print(f(n))

=======
Suggestion 4

def f(n):
    if n == 0:
        return 1
    else:
        return n * f(n - 1)

=======
Suggestion 5

def f(n):
    if n == 0:
        return 1
    else:
        return n * f(n-1)

n = int(input())
print(f(n))

=======
Suggestion 6

def f(x):
    if x == 0:
        return 1
    else:
        return x * f(x-1)

n = int(input())
print(f(n))

=======
Suggestion 7

def f(x):
    if x == 0:
        return 1
    else:
        return x * f(x - 1)

print(f(10))
