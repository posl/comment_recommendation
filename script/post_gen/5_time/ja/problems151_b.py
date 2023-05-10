Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N,K,M = map(int,input().split())
    A = list(map(int,input().split()))
    sum = 0
    for i in range(N-1):
        sum += A[i]
    if M*N <= sum:
        print(0)
    elif M*N - sum > K:
        print(-1)
    else:
        print(M*N - sum)

=======
Suggestion 2

def main():
    n,k,m = map(int,input().split())
    a = list(map(int,input().split()))
    sum = sum(a)
    if n*m - sum <= k:
        print(max(0,n*m - sum))
    else:
        print(-1)

=======
Suggestion 3

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    print(max(0, N * M - sum(A)) if N * M - sum(A) <= K else -1)

=======
Suggestion 4

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    if M * N - sum(A) > K:
        print(-1)
    else:
        print(max(0, M * N - sum(A)))

=======
Suggestion 5

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))

    sum = 0
    for i in range(N-1):
        sum += A[i]

    if N*M - sum <= K:
        print(max(N*M - sum, 0))
    else:
        print(-1)

=======
Suggestion 6

def solve():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    if N * M - sum(A) <= K:
        print(max(N * M - sum(A), 0))
    else:
        print(-1)

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

def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = max(0, m*n - sum(a))
    print(ans if ans <= k else -1)

=======
Suggestion 9

def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n-1):
        sum += a[i]
    if sum >= n*m:
        print(0)
    elif k*n - sum <= k:
        print(k*n - sum)
    else:
        print(-1)

=======
Suggestion 10

def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    if n*m - sum(a) <= k:
        print(max(0, n*m - sum(a)))
    else:
        print(-1)
