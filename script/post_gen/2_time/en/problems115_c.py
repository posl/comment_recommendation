Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    h = [int(input()) for _ in range(n)]
    h.sort()
    ans = 10**9
    for i in range(n-k+1):
        ans = min(ans, h[i+k-1]-h[i])
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    h = [int(input()) for _ in range(N)]
    h.sort()
    ans = 10 ** 9
    for i in range(N - K + 1):
        ans = min(ans, h[i + K - 1] - h[i])
    print(ans)

=======
Suggestion 3

def solve(n, k, h):
    h.sort()
    ans = 10 ** 9
    for i in range(n - k + 1):
        ans = min(ans, h[i + k - 1] - h[i])
    return ans

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    h = [int(input()) for _ in range(N)]
    h.sort()
    ans = 10 ** 9 + 1
    for i in range(N - K + 1):
        ans = min(ans, h[i + K - 1] - h[i])
    print(ans)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    h = sorted([int(input()) for i in range(n)])
    ans = float('inf')
    for i in range(n-k+1):
        ans = min(ans, h[i+k-1]-h[i])
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    h = sorted([int(input()) for _ in range(N)])
    min_diff = 10 ** 9
    for i in range(N - K + 1):
        min_diff = min(min_diff, h[i + K - 1] - h[i])
    print(min_diff)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    H = []
    for i in range(N):
        H.append(int(input()))

    H.sort()
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans, H[i+K-1]-H[i])
    print(ans)

=======
Suggestion 8

def read_input():
    N, K = map(int, input().split())
    H = [int(input()) for _ in range(N)]
    return N, K, H

=======
Suggestion 9

def   solve ( n , k , h ) 
     # write your code from here
 end
