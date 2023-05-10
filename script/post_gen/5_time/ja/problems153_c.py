Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort()
    if K >= N:
        print(0)
    else:
        print(sum(H[:N-K]))

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort(reverse=True)
    if K >= N:
        print(0)
    else:
        print(sum(H[K:]))

=======
Suggestion 3

def solve(n, k, h):
    h.sort()
    ans = 0
    for i in range(n - k):
        ans += h[i]
    return ans

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort(reverse=True)
    ans = 0
    for i in range(N):
        if i < K:
            continue
        ans += H[i]
    print(ans)

=======
Suggestion 5

def solve():
    N,K = map(int,input().split())
    H = list(map(int,input().split()))

    H.sort(reverse=True)
    if K >= N:
        print(0)
    else:
        print(sum(H[K:]))

=======
Suggestion 6

def solve():
    N,K = map(int,input().split())
    H = list(map(int,input().split()))
    H.sort(reverse=True)
    if N <= K:
        print(0)
    else:
        print(sum(H[K:]))

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    h = list(map(int,input().split()))
    h.sort()
    if k >= n:
        print(0)
    else:
        print(sum(h[:n-k]))

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort(reverse=True)
    print(sum(h[k:]))

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort(reverse=True)
    ans = sum(H[K:])
    print(ans)

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort(reverse=True)
    print(sum(H[K:]))
