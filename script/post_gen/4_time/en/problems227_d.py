Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    print(sum(A[:K]))

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    a = sorted(map(int, input().split()))
    print(sum(a[-k:]))

=======
Suggestion 3

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    print(sum(A[:K]))
    return 0

=======
Suggestion 4

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if i < k:
            ans += a[i]
    print(ans)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    a = sorted(map(int, input().split()), reverse=True)
    print(n - sum(a[:k]))

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    #print(A)
    ans = 0
    for i in range(K):
        ans += A[i]
    print(ans)
    return
