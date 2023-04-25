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
    n, a, b = map(int, input().split())
    if n % (a + b) <= a:
        print((n // (a + b)) * a + n % (a + b))
    else:
        print((n // (a + b)) * a + a)

=======
Suggestion 4

def main():
    n, a, b = map(int, input().split())
    print(n // (a + b) * a + min(n % (a + b), a))

=======
Suggestion 5

def main():
    N, A, B = map(int, input().split())
    print((N // (A + B)) * A + min(A, N % (A + B)))

=======
Suggestion 6

def solve():
    N, A, B = map(int, input().split())
    if N % (A + B) <= A and N % (A + B) != 0:
        print(N // (A + B) * A + N % (A + B))
    else:
        print(N // (A + B) * A + A)

=======
Suggestion 7

def main():
    n, a, b = map(int, input().split())
    if a == 0:
        print(0)
    elif a+b >= n:
        print(a)
    else:
        print(a*(n//(a+b)) + min(a, n%(a+b)))

=======
Suggestion 8

def main():
    N, A, B = map(int, input().split())
    blue = N//(A+B)
    remain = N%(A+B)
    if remain <= A:
        print(blue*A+remain)
    else:
        print(blue*A+A)

=======
Suggestion 9

def solve():
    N,A,B = map(int, input().split())
    print((N//(A+B))*A + min(N%(A+B), A))
