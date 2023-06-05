Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, a, b = map(int, input().split())

    if a + b == 0:
        print(0)
    else:
        print(n // (a + b) * a + min(n % (a + b), a))

=======
Suggestion 2

def main():
    n,a,b = map(int, input().split())
    print(n//(a+b)*a + min(a, n%(a+b)))

=======
Suggestion 3

def main():
    n, a, b = map(int, input().split())
    if a > b:
        print(0)
    elif a == b:
        print(1)
    else:
        print(n * a // (a + b))

=======
Suggestion 4

def solution1():
    N, A, B = map(int, input().split())
    if A + B == 0:
        print(0)
        return
    if N == 1:
        if A > 0:
            print(1)
        else:
            print(0)
        return
    if A == 0:
        print(0)
        return
    if B == 0:
        print(1)
        return
    if N <= A:
        print(N)
        return
    if N == A + 1:
        print(A)
        return
    if N == A + 2:
        print(A + 1)
        return
    if A <= N <= A + B:
        print(A)
        return
    if N == A + B + 1:
        print(A + 1)
        return
    if N == A + B + 2:
        print(A + 2)
        return
    if A + B + 3 <= N <= 2 * A + B + 2:
        print(N - A - 1)
        return
    if N == 2 * A + B + 3:
        print(A + 1)
        return
    if N == 2 * A + B + 4:
        print(A + 2)
        return
    if 2 * A + B + 5 <= N <= 2 * A + 2 * B + 4:
        print(A + 2)
        return
    if N == 2 * A + 2 * B + 5:
        print(A + 2)
        return
    if N == 2 * A + 2 * B + 6:
        print(A + 3)
        return
    if 2 * A + 2 * B + 7 <= N <= 3 * A + 2 * B + 6:
        print(A + 3)
        return
    if N == 3 * A + 2 * B + 7:
        print(A + 3)
        return
    if N == 3 * A + 2 * B + 8:
        print(A + 4)
        return
    if 3 * A + 2 * B + 9 <= N <= 3 * A + 3 * B + 8:
        print(A

=======
Suggestion 5

def main():
    N, A, B = map(int, input().split())
    if N <= A + B:
        print(min(A, N))
    else:
        print(A + (N - A - B) * (A - B))

=======
Suggestion 6

def problem158_b():
    n, a, b = map(int, input().split())
    if a+b == 0:
        print(0)
        return
    if a == 0:
        print(0)
        return
    if n <= a+b:
        print(n)
        return
    else:
        print(a+(n-a-b)*b)

=======
Suggestion 7

def f(n, a, b):
    if n <= a:
        return n
    else:
        return a + (n - a) * b

=======
Suggestion 8

def main():
    N,A,B = map(int,input().split())
    b = N//(A+B)
    r = N%(A+B)
    print(b*A+r if r<=A else b*A+A)

=======
Suggestion 9

def main():
    N, A, B = map(int, input().split())
    if A == 0:
        print(0)
    elif B == 0:
        print(N)
    else:
        print(N // (A + B) * A + min(N % (A + B), A))

=======
Suggestion 10

def main():
    N, A, B = map(int, input().split())
    n = N // (A + B)
    r = N % (A + B)
    print(n * A + min(r, A))
