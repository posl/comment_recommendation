Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    for i in range(K):
        if N % 200 == 0:
            N = N // 200
        else:
            N = int(str(N) + "200")
    print(N)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    for i in range(K):
        if N % 200 == 0:
            N = N // 200
        else:
            N = int(str(N) + '200')
    print(N)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    for _ in range(k):
        if n % 200 == 0:
            n = n // 200
        else:
            n = int(str(n) + '200')
    print(n)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    for _ in range(k):
        if n % 200 == 0:
            n //= 200
        else:
            n = int(str(n) + "200")
    print(n)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    for i in range(k):
        if n % 200 == 0:
            n //= 200
        else:
            n = int(str(n) + "200")
    print(n)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    for i in range(k):
        if n % 200 == 0:
            n //= 200
        else:
            n = int(str(n) + '200')
    print(n)

=======
Suggestion 7

def problems200_b():
    n, k = map(int, input().split())
    for _ in range(k):
        if n % 200 == 0:
            n = n // 200
        else:
            n = int(str(n) + "200")
    print(n)

=======
Suggestion 8

def solve(n, k):
    for i in range(k):
        if n % 200 == 0:
            n = n // 200
        else:
            n = int(str(n) + '200')
    return n

=======
Suggestion 9

def main():
    n,k = map(int, input().split())
    for i in range(k):
        if n % 200 == 0:
            n = n // 200
        else:
            n = int(str(n) + "200")
    print(n)

=======
Suggestion 10

def solve(N, K):
    for i in range(K):
        if N % 200 == 0:
            N = N // 200
        else:
            N = int(str(N) + '200')
    return N
