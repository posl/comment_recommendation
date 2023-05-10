Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(M):
        sum += A[i]
    if sum <= N:
        print(N - sum)
    else:
        print(-1)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    if sum(A) > N:
        print(-1)
    else:
        print(N - sum(A))

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    if n < sum(a):
        print(-1)
    else:
        print(n - sum(a))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    if N < sum(A):
        print(-1)
    else:
        print(N - sum(A))

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(M):
        sum += A[i]
    if N < sum:
        print(-1)
    else:
        print(N-sum)

=======
Suggestion 6

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    if sum(a) > n:
        print(-1)
    else:
        print(n - sum(a))

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    print(n - sum(a) if n >= sum(a) else -1)

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = n
    for i in range(m):
        ans -= a[i]
    print(-1 if ans < 0 else ans)
