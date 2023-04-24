Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10 ** 9
    for i in range(N - K + 1):
        ans = min(ans, abs(X[i]) + abs(X[i + K - 1] - X[i]))
        ans = min(ans, abs(X[i + K - 1]) + abs(X[i + K - 1] - X[i]))
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans, abs(x[i])+abs(x[i+K-1]-x[i]), abs(x[i+K-1])+abs(x[i+K-1]-x[i]))
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10**18
    for i in range(N-K+1):
        ans = min(ans, x[i+K-1] - x[i] + min(abs(x[i]), abs(x[i+K-1])))
    print(ans)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10**9
    for i in range(n-k+1):
        ans = min(ans, x[i+k-1] - x[i] + min(abs(x[i]), abs(x[i+k-1])))
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans, min(abs(x[i]), abs(x[i+K-1])) + abs(x[i+K-1]-x[i]))
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10**18
    for i in range(N-K+1):
        ans = min(ans, abs(X[i])+abs(X[i]-X[i+K-1]), abs(X[i+K-1])+abs(X[i+K-1]-X[i]))
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans, min(X[i+K-1]+X[i], abs(X[i])+abs(X[i+K-1]-X[i])))

    print(ans)

=======
Suggestion 8

def main():
    N, K = [int(x) for x in input().split()]
    X = [int(x) for x in input().split()]
    ans = float('inf')
    for i in range(N - K + 1):
        ans = min(ans, X[i + K - 1] - X[i] + min(abs(X[i]), abs(X[i + K - 1])))
    print(ans)

=======
Suggestion 9

def solve():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = float("inf")
    for i in range(N-K+1):
        ans = min(ans, X[i+K-1]-X[i]+min(abs(X[i]), abs(X[i+K-1])))
    print(ans)

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10**18
    for i in range(N-K+1):
        # 左に移動
        left = X[i]
        # 右に移動
        right = X[i+K-1]
        # 0 から左に移動
        if left >= 0:
            ans = min(ans, right)
        # 0 から右に移動
        elif right <= 0:
            ans = min(ans, -left)
        # 0 から左右に移動
        else:
            ans = min(ans, min(abs(left), abs(right)) + right - left)
    print(ans)
