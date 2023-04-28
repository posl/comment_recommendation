Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    print(sum(a[:k]))

=======
Suggestion 2

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    print(sum(A[0:K]))

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    A.sort(reverse=True)

    print(sum(A[:K]))

=======
Suggestion 4

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    ans = 0
    for i in range(N-K+1):
        ans = max(ans, A[i+K-1]-A[i])
    print(ans)

=======
Suggestion 5

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    print(sum(A[-K:]))
    return 0

=======
Suggestion 6

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)

    ans = 0
    for a in A[:K]:
        ans += a
    print(ans)

=======
Suggestion 7

def solve(n, k, a):
    a.sort(reverse=True)
    return sum(a[:k])
