Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    h = [int(input()) for _ in range(n)]
    h.sort()
    ans = h[-1] - h[0]
    for i in range(n-k+1):
        ans = min(ans, h[i+k-1] - h[i])
    print(ans)

=======
Suggestion 2

def main():
    n,k = map(int,input().split())
    h = [int(input()) for _ in range(n)]
    h.sort()
    ans = h[k-1] - h[0]
    for i in range(n-k+1):
        ans = min(ans,h[i+k-1]-h[i])
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    H = [int(input()) for _ in range(N)]
    H.sort()
    ans = 10 ** 9
    for i in range(N - K + 1):
        ans = min(ans, H[i + K - 1] - H[i])
    print(ans)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    h = [int(input()) for _ in range(n)]
    h.sort()
    ans = 10**9
    for i in range(n-k+1):
        ans = min(ans, h[i+k-1] - h[i])
    print(ans)

=======
Suggestion 5

def main():
    n,k = map(int,input().split())
    h_list = []
    for i in range(n):
        h_list.append(int(input()))
    h_list.sort()
    min = h_list[0]
    max = h_list[k-1]
    for i in range(n-k):
        if h_list[i+k-1] - h_list[i] < max - min:
            min = h_list[i]
            max = h_list[i+k-1]
    print(max-min)

=======
Suggestion 6

def solve():
    N, K = map(int, input().split())
    h = [int(input()) for _ in range(N)]
    h.sort()
    ans = h[K-1] - h[0]
    for i in range(1, N-K+1):
        ans = min(ans, h[i+K-1] - h[i])
    print(ans)

=======
Suggestion 7

def main():
    n,k = map(int, input().split())
    h = []
    for _ in range(n):
        h.append(int(input()))
    h.sort()
    ans = 10**9
    for i in range(n-k+1):
        ans = min(ans, h[i+k-1]-h[i])
    print(ans)

=======
Suggestion 8

def main():
    n,k = map(int,input().split())
    h = [int(input()) for i in range(n)]
    h.sort()
    ans = 10**9
    for i in range(n-k+1):
        ans = min(ans,h[i+k-1]-h[i])
    print(ans)

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    h = [int(input()) for _ in range(n)]
    h.sort()
    print(min(h[i+k-1]-h[i] for i in range(n-k+1)))
