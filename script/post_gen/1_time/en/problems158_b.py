Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, A, B = map(int, input().split())
    if N % (A + B) <= A:
        print(N // (A + B) * A + N % (A + B))
    else:
        print(N // (A + B) * A + A)

=======
Suggestion 2

def main():
    N, A, B = map(int, input().split())
    print((N // (A + B)) * A + min(N % (A + B), A))

=======
Suggestion 3

def main():
    N, A, B = map(int, input().split())
    print((N // (A + B)) * A + min(A, N % (A + B)))

=======
Suggestion 4

def main():
    N, A, B = map(int, input().split())
    x = N // (A + B)
    y = N % (A + B)
    print(x * A + min(y, A))

=======
Suggestion 5

def main():
    N, A, B = map(int, input().split())
    if A == 0:
        print(0)
    elif B == 0:
        print(N)
    else:
        print(A * (N // (A + B)) + min(A, N % (A + B)))

=======
Suggestion 6

def main():
    N, A, B = map(int, input().split())
    if A == 0:
        print(0)
        return
    if B == 0:
        print(N)
        return
    print((N // (A + B)) * A + min(N % (A + B), A))

=======
Suggestion 7

def solve(n, a, b):
    if a == 0:
        return 0
    elif b == 0:
        return n
    else:
        return (n // (a + b)) * a + min(a, n % (a + b))

=======
Suggestion 8

def solve(n, a, b):
    if n <= (a + b):
        return min(a, n)
    else:
        return a + (n - (a + b)) * (a - b)
