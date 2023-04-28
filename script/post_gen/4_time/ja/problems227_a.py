Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K, A = map(int, input().split())
    print((K - 1 + A - 1) % N + 1)

=======
Suggestion 2

def main():
    # input
    n, k, a = map(int, input().split())

    # compute

    # output
    if k % n == 0:
        print(n)
    else:
        print(k % n)

=======
Suggestion 3

def main():
    n, k, a = map(int, input().split())
    if k % n == 0:
        print(a)
    else:
        print(a + (k % n) - 1 if a + (k % n) <= n else a + (k % n) - n)

=======
Suggestion 4

def main():
    n, k, a = map(int, input().split())
    print((k + a - 1) % n + 1)

=======
Suggestion 5

def main():
    n, k, a = map(int, input().split())
    if k % n == 0:
        print(a)
    else:
        print((k % n) + a)

=======
Suggestion 6

def main():
    N, K, A = map(int, input().split())
    result = (K - (N - A + 1)) % N
    print(N if result == 0 else result)

=======
Suggestion 7

def main():
    n, k, a = map(int, input().split())
    if k % n == 0:
        print(a)
    else:
        print(k % n)

=======
Suggestion 8

def main():
    n, k, a = map(int, input().split())
    print((k-1+a-1)%n+1)

=======
Suggestion 9

def problem227_a():
    N, K, A = map(int, input().split())
    print((K - 1 + A - 1) % N + 1)
    return

=======
Suggestion 10

def main():
    n, k, a = map(int, input().split())
    if k >= n:
        k = k % n
    if k < n:
        if a + k > n:
            print(a + k - n)
        else:
            print(a + k)
