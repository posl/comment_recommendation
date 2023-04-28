Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    h = [int(input()) for _ in range(N)]
    h.sort()
    print(min(h[i+K-1]-h[i] for i in range(N-K+1)))

main()

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    h = [int(input()) for _ in range(n)]
    h.sort()
    print(min(h[i + k - 1] - h[i] for i in range(n - k + 1)))

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    h = [int(input()) for _ in range(N)]
    h.sort()
    print(min(h[i+K-1] - h[i] for i in range(N-K+1)))

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    h = [int(input()) for _ in range(N)]
    h.sort()
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans, h[i+K-1]-h[i])
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    h = [int(input()) for _ in range(N)]
    h.sort()
    ans = h[K-1] - h[0]
    for i in range(1, N-K+1):
        ans = min(ans, h[K-1+i] - h[i])
    print(ans)

=======
Suggestion 6

def main():
    n,k = map(int, input().split())
    h = [int(input()) for _ in range(n)]
    h.sort()
    ans = 10**9
    for i in range(n-k+1):
        ans = min(ans, h[i+k-1]-h[i])
    print(ans)

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    h = [int(input()) for _ in range(n)]
    h.sort()
    ans = h[n-1] - h[0]
    for i in range(n-k+1):
        ans = min(ans,h[i+k-1]-h[i])
    print(ans)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    h = [int(input()) for i in range(N)]
    h.sort()
    ans = 10000000000000
    for i in range(N-K+1):
        ans = min(ans, h[i+K-1]-h[i])
    print(ans)
main()

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort()
    print(h[K-1] - h[0])
