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
        return x * f(x-1)

N = int(input())
print(f(N))

=======
Suggestion 3

def f(x):
    if x == 0:
        return 1
    return x * f(x - 1)

N = int(input())
print(f(N))

=======
Suggestion 4

def f(num):
    if num == 0:
        return 1
    else:
        return num * f(num - 1)

=======
Suggestion 5

def main():
    N = int(input())
    print(fact(N))
