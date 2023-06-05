Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def problem198_a():
    n = int(input())
    if n < 3:
        print(0)
    else:
        print(int((n-1)*(n-2)/2))

=======
Suggestion 2

def f(n):
    return n * (n + 1) // 2

n = int(input())
print(f(n-1))

=======
Suggestion 3

def main():
    N = int(input())
    print(N-1)

=======
Suggestion 4

def main():
    n = int(input())
    print(n-1)

=======
Suggestion 5

def main():
    n = int(input())
    if n % 2 == 0:
        print(int(n/2 - 1))
    else:
        print(int(n/2))

=======
Suggestion 6

def solve():
    N = int(input())
    print(N-1)

=======
Suggestion 7

def main():
    N = int(input())
    if N%2 == 0:
        print(int(N/2 - 1))
    else:
        print(int((N-1)/2))

=======
Suggestion 8

def solve():
    n = int(input())
    print((n-1) if n > 1 else 0)
