Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,k = map(int,input().split())
    h = [int(input()) for i in range(n)]
    h.sort()
    min = 10**9
    for i in range(n-k+1):
        if h[i+k-1]-h[i] < min:
            min = h[i+k-1]-h[i]
    print(min)

=======
Suggestion 2

def main():
    n,k = map(int,input().split())
    h = sorted([int(input()) for _ in range(n)])
    ans = 10**9
    for i in range(n-k+1):
        ans = min(ans,h[i+k-1]-h[i])
    print(ans)

=======
Suggestion 3

def main():
    n,k = map(int, input().split())
    h = [int(input()) for _ in range(n)]
    h.sort()
    min = 10**9
    for i in range(n-k+1):
        if h[i+k-1] - h[i] < min:
            min = h[i+k-1] - h[i]
    print(min)

=======
Suggestion 4

def main():
    n,k = map(int,input().split())
    h = [int(input()) for _ in range(n)]
    h.sort()
    print(min(h[i+k-1]-h[i] for i in range(n-k+1)))

=======
Suggestion 5

def main():
    n,k = map(int,input().split())
    h = [int(input()) for _ in range(n)]
    h.sort()
    ans = 10**9
    for i in range(n-k+1):
        ans = min(ans,h[i+k-1]-h[i])
    print(ans)

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    h = [int(input()) for i in range(n)]
    h.sort()
    min = h[k-1] - h[0]
    for i in range(n-k+1):
        if h[i+k-1] - h[i] < min:
            min = h[i+k-1] - h[i]
    print(min)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    h = [int(input()) for _ in range(n)]
    h.sort()
    ans = min(h[i+k-1]-h[i] for i in range(n-k+1))
    print(ans)

=======
Suggestion 9

def solve():
    N, K = map(int, input().split())
    H = []
    for i in range(N):
        H.append(int(input()))
    H.sort()
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans, H[i+K-1]-H[i])
    print(ans)
