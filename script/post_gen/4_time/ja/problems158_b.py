Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, a, b = map(int, input().split())
    print(n // (a + b) * a + min(n % (a + b), a))

=======
Suggestion 2

def main():
    n, a, b = map(int, input().split())
    print((n // (a+b)) * a + min(n % (a+b), a))

=======
Suggestion 3

def main():
    N, A, B = map(int, input().split())
    if N % (A + B) == 0:
        print(A * (N // (A + B)))
    else:
        print(A * (N // (A + B)) + min(A, N % (A + B)))

=======
Suggestion 4

def main():
    n, a, b = map(int, input().split())
    print((n // (a+b)) * a + min((n % (a+b)), a))

=======
Suggestion 5

def main():
    n, a, b = map(int, input().split())
    if a+b == 0:
        print(0)
    else:
        print(a*(n//(a+b))+min(a, n%(a+b)))

=======
Suggestion 6

def main():
    N, A, B = map(int, input().split())
    if N <= A + B:
        print(min(A, N))
    else:
        print(A + (N - A - B) * (A - B))

=======
Suggestion 7

def main():
    N, A, B = map(int, input().split())
    blue_balls = N // (A + B) * A
    remain_balls = N % (A + B)
    if remain_balls > A:
        print(blue_balls + A)
    else:
        print(blue_balls + remain_balls)

=======
Suggestion 8

def main():
    n, a, b = map(int, input().split())
    if a == 0:
        print(0)
    elif n <= a+b:
        print(min(a, n))
    else:
        print(min(a, n-a-b))

=======
Suggestion 9

def main():
    n, a, b = map(int, input().split())
    #print(n, a, b)
    if a + b == 0:
        print(0)
    else:
        print((n // (a + b)) * a + min(n % (a + b), a))

=======
Suggestion 10

def main():
    n,a,b = map(int, input().split())
    #print(n,a,b)
    if a+b == 0:
        print(0)
        exit()
    if a == 0:
        print(n)
        exit()
    if n == 1:
        print(1)
        exit()
    if a+b > n:
        print(n)
        exit()
    if a+b == n:
        print(a)
        exit()
    if a+b < n:
        print(a)
        exit()
