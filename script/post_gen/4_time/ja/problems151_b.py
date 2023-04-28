Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    if n * m - sum(a) > k:
        print(-1)
    else:
        print(max(n * m - sum(a), 0))

=======
Suggestion 2

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N-1):
        sum += A[i]
    if M * N - sum > K:
        print(-1)
    elif M * N - sum <= 0:
        print(0)
    else:
        print(M * N - sum)

=======
Suggestion 3

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N-1):
        sum += A[i]
    if N*M - sum > K:
        print(-1)
    else:
        print(max(0, N*M - sum))

=======
Suggestion 4

def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))

    sum = 0
    for i in range(n-1):
        sum += a[i]

    if n*m - sum <= k:
        print(max(n*m - sum, 0))
    else:
        print(-1)

=======
Suggestion 5

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    if N * M - sum(A) <= K:
        if N * M - sum(A) >= 0:
            print(N * M - sum(A))
        else:
            print(0)
    else:
        print(-1)

=======
Suggestion 6

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    X = N * M - sum(A)
    if X > K:
        print(-1)
    elif X < 0:
        print(0)
    else:
        print(X)

=======
Suggestion 7

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    total = sum(A)
    if N * M - total > K:
        print(-1)
    else:
        print(max(0, N * M - total))

=======
Suggestion 8

def solve():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    X = N*M - sum(A)
    if X > K:
        return -1
    else:
        return max(0, X)

print(solve())

=======
Suggestion 9

def main():
    n,k,m = map(int,input().split())
    A = list(map(int,input().split()))
    sum = 0
    for i in range(n-1):
        sum += A[i]
    if n*m-sum > k:
        print(-1)
    else:
        if n*m-sum < 0:
            print(0)
        else:
            print(n*m-sum)

=======
Suggestion 10

def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))

    total = sum(a)
    t = n * m - total
    if t > k:
        print(-1)
    else:
        print(max(0, t))
