Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    if (N - 1) % (K - 1) == 0:
        print((N - 1) // (K - 1))
    else:
        print((N - 1) // (K - 1) + 1)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if n % (k - 1) == 0:
        print(n // (k - 1) - 1)
    else:
        print(n // (k - 1))

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    ans += (n - 1) // (k - 1)
    if (n - 1) % (k - 1) != 0:
        ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    if N % (K-1) == 0:
        print(N // (K-1))
    else:
        print(N // (K-1) + 1)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    while n > 0:
        n -= k
        ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += (a[i] - 1) // (k - 1)
    print(ans)

=======
Suggestion 7

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    print((N-2)//(K-1) + 1)

=======
Suggestion 8

def main():
    N,K = map(int, input().split())
    A = list(map(int, input().split()))

    count = 0
    for i in range(N-K):
        if A[i] != A[i+K]:
            count += 1
    print(count)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    A = A[:N - 1]
    print((N + K - 3) // (K - 1))
