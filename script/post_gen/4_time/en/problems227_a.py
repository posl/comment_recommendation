Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k, a = map(int, input().split())
    if (k - a) % (n - 1) == 0:
        print(n)
    else:
        print((k - a) % (n - 1) + a)

=======
Suggestion 2

def main():
    N, K, A = map(int, input().split())
    print((K - N) // (N - 1) + 1 if (K - N) % (N - 1) else (K - N) // (N - 1))

=======
Suggestion 3

def main():
    N, K, A = map(int, input().split())
    if K <= N:
        print(K)
    else:
        print(N - (K - N) % (N - A + 1))

=======
Suggestion 4

def main():
    n, k, a = map(int, input().split())
    if k <= n:
        print(k)
    else:
        k = k - n
        print(n - (k % n))

=======
Suggestion 5

def main():
    n, k, a = map(int, input().split())
    if k < n:
        print(k)
    else:
        print(k % n)

=======
Suggestion 6

def main():
    N, K, A = map(int, input().split())
    print((K // N + (K % N >= A)) % N or N)

=======
Suggestion 7

def main():
    n,k,a = map(int, input().split())
    print(1 + (k - a - 1) // (n - a))

=======
Suggestion 8

def main():
    N, K, A = map(int, input().split())
    print(int((K - A - 1) / (N - 1)) + 1)

=======
Suggestion 9

def problem227_a():
    n, k, a = map(int, input().split())
    print((k - a) % (n - a) + a)

=======
Suggestion 10

def main():
    n, k, a = map(int, input().split())
    if (n-a) >= (k-n):
        print(k-n+a)
    else:
        print(a+k-n)
