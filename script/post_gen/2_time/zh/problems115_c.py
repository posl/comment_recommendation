Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,k = map(int,input().split())
    h = [int(input()) for i in range(n)]
    h.sort()
    ans = 1000000000
    for i in range(n-k+1):
        ans = min(ans,h[i+k-1]-h[i])
    print(ans)

=======
Suggestion 2

def f(n,k,h):
    h.sort()
    return h[k-1]-h[0]

n,k=map(int,input().split())
h=[int(input()) for i in range(n)]
print(f(n,k,h))

=======
Suggestion 3

def main():
    n,k = map(int, input().split())
    h = [int(input()) for _ in range(n)]
    h.sort()
    ans = 10**9
    for i in range(n-k+1):
        ans = min(ans, h[i+k-1]-h[i])
    print(ans)

=======
Suggestion 4

def main():
    N,K = map(int,input().split())
    h = [int(input()) for i in range(N)]
    h.sort()
    ans = h[K-1]-h[0]
    for i in range(1,N-K+1):
        if ans > h[i+K-1]-h[i]:
            ans = h[i+K-1]-h[i]
    print(ans)

=======
Suggestion 5

def resolve():
    N,K = map(int,input().split())
    h = []
    for i in range(N):
        h.append(int(input()))
    h.sort()
    ans = 10**9
    for i in range(N-K+1):
        tmp = h[i+K-1]-h[i]
        if tmp < ans:
            ans = tmp
    print(ans)

=======
Suggestion 6

def solve():
    N,K = map(int,input().split())
    h = [int(input()) for _ in range(N)]
    h.sort()
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans,h[i+K-1]-h[i])
    print(ans)

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    h = [int(input()) for i in range(n)]
    h.sort()
    ans = float('inf')
    for i in range(n-k+1):
        ans = min(ans, h[i+k-1]-h[i])
    print(ans)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    h = [int(input()) for _ in range(n)]
    h.sort()
    print(min(h[i+k-1]-h[i] for i in range(n-k+1)))
