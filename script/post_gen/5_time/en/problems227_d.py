Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    #import sys
    #input = sys.stdin.readline
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    ans = 0
    for i in range(n):
        if i < k:
            continue
        ans += a[i]
    print(ans)
    return 0

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n-k):
        ans += a[i]
    print(ans)

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
    print(sum(A[-K:]))
    return 0

=======
Suggestion 5

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    print(N - sum(A[:K]))

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    print(sum(A[:k]))

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    total = sum(a)
    if k >= n:
        print(0)
    else:
        print(total - sum(a[-k:]))

=======
Suggestion 8

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    a.reverse()
    s = sum(a[:k])
    print(s)

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    if n == k:
        print(1)
        return

    a.sort()
    a.reverse()

    print((n-1 + k - 2) // (k - 1))

main()

=======
Suggestion 10

def solve(N, K, A):
    A.sort(reverse=True)
    ans = 0
    if N == K:
        return 1
    for i in range(N):
        if i < K:
            ans += A[i]
    return ans
