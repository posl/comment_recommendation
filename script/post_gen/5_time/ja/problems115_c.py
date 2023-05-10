Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,k = map(int,input().split())
    h = [int(input()) for i in range(n)]
    h = sorted(h)
    ans = h[-1] - h[0]
    for i in range(n-k+1):
        ans = min(ans,h[i+k-1]-h[i])
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    h = [int(input()) for _ in range(N)]
    h.sort()
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans, h[i+K-1]-h[i])
    print(ans)

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    h = [int(input()) for _ in range(n)]
    h.sort()
    ans = 10**9
    for i in range(n-k+1):
        ans = min(ans,h[i+k-1]-h[i])
    print(ans)

=======
Suggestion 4

def solve():
    N, K = map(int, input().split())
    h = [int(input()) for _ in range(N)]
    h.sort()
    ans = 10**9
    for i in range(N - K + 1):
        ans = min(ans, h[i + K - 1] - h[i])
    print(ans)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    h = []
    for i in range(n):
        h.append(int(input()))
    h.sort()
    ans = 10**9
    for i in range(n-k+1):
        ans = min(ans, h[i+k-1]-h[i])
    print(ans)

=======
Suggestion 6

def main():
    n,k = map(int,input().split())
    h = [int(input()) for i in range(n)]
    h.sort()
    ans = 10**9
    for i in range(n-k+1):
        ans = min(ans,h[i+k-1]-h[i])
    print(ans)
main()

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    h = [int(input()) for _ in range(n)]
    h.sort()
    min_diff = float('inf')
    for i in range(n-k+1):
        diff = h[i+k-1] - h[i]
        min_diff = min(min_diff, diff)
    print(min_diff)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    H = [int(input()) for _ in range(N)]
    H.sort()
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans, H[i+K-1] - H[i])
    print(ans)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    h = [0] * N
    for i in range(N):
        h[i] = int(input())
    h.sort()
    min = h[K-1] - h[0]
    for i in range(N-K+1):
        if min > h[i+K-1] - h[i]:
            min = h[i+K-1] - h[i]
    print(min)
