Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    h = sorted([int(input()) for _ in range(n)])
    print(min(h[i+k-1]-h[i] for i in range(n-k+1)))

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    h = [int(input()) for _ in range(n)]
    h.sort()
    print(min(h[i+k-1]-h[i] for i in range(n-k+1)))

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    h = [int(input()) for _ in range(N)]
    h.sort()
    print(min(h[i+K-1]-h[i] for i in range(N-K+1)))

=======
Suggestion 4

def solve():
    N,K = map(int,input().split())
    h = [int(input()) for _ in range(N)]
    h.sort()
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans,h[i+K-1]-h[i])
    print(ans)
solve()

=======
Suggestion 5

def solve():
    N, K = map(int, input().split())
    h = [int(input()) for _ in range(N)]
    h.sort()

    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans, h[i+K-1] - h[i])
    print(ans)

=======
Suggestion 6

def main():
    n,k = map(int, input().split())
    h = sorted([int(input()) for i in range(n)])
    print(min([h[i+k-1]-h[i] for i in range(n-k+1)]))

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    h = [int(input()) for _ in range(n)]

    h.sort()

    ans = float('inf')
    for i in range(n - k + 1):
        ans = min(ans, h[i + k - 1] - h[i])

    print(ans)

=======
Suggestion 8

def solve(n, k, h):
    h.sort()
    return h[k-1] - h[0]
