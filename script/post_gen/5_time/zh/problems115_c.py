Synthesizing 10/10 solutions

=======
Suggestion 1

def get_input():
    n,k = map(int, input().split())
    h = [int(input()) for i in range(n)]
    return n,k,h

=======
Suggestion 2

def solve():
    n,k = map(int,input().split())
    h = [int(input()) for _ in range(n)]
    h = sorted(h)
    ans = 10**9
    for i in range(n-k+1):
        ans = min(ans,h[i+k-1]-h[i])
    print(ans)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    h = []
    for i in range(n):
        h.append(int(input()))
    h = sorted(h)
    ans = 10 ** 9
    for i in range(n - k + 1):
        ans = min(ans, h[i + k - 1] - h[i])
    print(ans)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    h = [int(input()) for _ in range(n)]
    h.sort()
    ans = h[k - 1] - h[0]
    for i in range(n - k + 1):
        ans = min(ans, h[i + k - 1] - h[i])
    print(ans)

=======
Suggestion 5

def main():
    N,K = map(int,input().split())
    h = [int(input()) for _ in range(N)]
    h.sort()
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans,h[i+K-1]-h[i])
    print(ans)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    h = [int(input()) for _ in range(n)]
    h.sort()
    ans = h[k-1] - h[0]
    for i in range(1, n-k+1):
        ans = min(ans, h[k-1+i]-h[i])
    print(ans)

main()

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    h = [int(input()) for _ in range(n)]
    h.sort()
    print(min(h[i+k-1]-h[i] for i in range(n-k+1)))

=======
Suggestion 8

def main():
    n,k = map(int, input().split())
    h = []
    for i in range(n):
        h.append(int(input()))
    h.sort()
    # print(h)
    min = h[k-1] - h[0]
    for i in range(n-k+1):
        if h[i+k-1] - h[i] < min:
            min = h[i+k-1] - h[i]
    print(min)

=======
Suggestion 9

def readinput():
    n,k=list(map(int,input().split()))
    h=list(map(int,input().split()))
    return n,k,h

=======
Suggestion 10

def main():
    n,k = map(int,input().split())
    h = []
    for i in range(n):
        h.append(int(input()))
    h.sort()
    ans = 10**9
    for i in range(n-k+1):
        ans = min(ans,h[i+k-1]-h[i])
    print(ans)
