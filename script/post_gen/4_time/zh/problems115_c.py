Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,k = map(int, input().split())
    h = []
    for i in range(n):
        h.append(int(input()))
    h.sort()
    ans = h[k-1] - h[0]
    for i in range(1,n-k+1):
        ans = min(ans, h[i+k-1] - h[i])
    print(ans)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    h = [int(input()) for _ in range(n)]
    h.sort()
    ans = float('inf')
    for i in range(n-k+1):
        ans = min(ans, h[i+k-1]-h[i])
    print(ans)

=======
Suggestion 3

def solve():
    N, K = map(int, input().split())
    h = [int(input()) for _ in range(N)]
    h.sort()
    print(h[K-1] - h[0])

solve()

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

def solve():
    n, k = map(int, input().split())
    h = [int(input()) for _ in range(n)]
    h.sort()
    ans = h[k-1] - h[0]
    for i in range(1, n-k+1):
        ans = min(ans, h[i+k-1] - h[i])
    print(ans)

solve()

=======
Suggestion 6

def solve():
    n,k = map(int,input().split())
    h = [int(input()) for _ in range(n)]
    h.sort()
    ans = 10**10
    for i in range(n-k+1):
        ans = min(ans,h[i+k-1]-h[i])
    print(ans)
solve()

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    h = [int(input()) for i in range(n)]
    h.sort()
    ans = 10 ** 9
    for i in range(n - k + 1):
        ans = min(ans, h[i + k - 1] - h[i])
    print(ans)

=======
Suggestion 8

def main():
    n,k=map(int,input().split())
    h=[]
    for i in range(n):
        h.append(int(input()))
    h.sort()
    ans=10**9
    for i in range(n-k+1):
        ans=min(ans,h[i+k-1]-h[i])
    print(ans)

=======
Suggestion 9

def main():
    N,K = map(int,input().split())
    h = []
    for i in range(N):
        h.append(int(input()))
    h.sort()
    min = h[K-1] - h[0]
    for i in range(1,N-K+1):
        if min > h[i+K-1] - h[i]:
            min = h[i+K-1] - h[i]
    print(min)

=======
Suggestion 10

def solve():
    n, k = map(int, input().split())
    h = [int(input()) for _ in range(n)]
    h.sort()
    ans = h[k-1] - h[0]
    for i in range(n-k+1):
        ans = min(ans, h[i+k-1] - h[i])
    print(ans)
