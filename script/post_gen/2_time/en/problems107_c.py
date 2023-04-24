Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    ans = float('inf')
    for i in range(N - K + 1):
        ans = min(ans, abs(x[i]) + abs(x[i + K - 1] - x[i]), abs(x[i + K - 1]) + abs(x[i + K - 1] - x[i]))
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10 ** 18
    for i in range(N - K + 1):
        ans = min(ans, abs(x[i]) + abs(x[i] - x[i + K - 1]), abs(x[i + K - 1]) + abs(x[i] - x[i + K - 1]))
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    ans = float('inf')
    for i in range(N-K+1):
        ans = min(ans, abs(x[i])+abs(x[i]-x[i+K-1]), abs(x[i+K-1])+abs(x[i+K-1]-x[i]))
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    ans = float('inf')
    for i in range(N-K+1):
        left = x[i]
        right = x[i+K-1]
        if left >= 0:
            ans = min(ans, right - left)
        elif right <= 0:
            ans = min(ans, abs(left) + abs(right))
        else:
            ans = min(ans, abs(left) + right + min(abs(left), right))
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10**18
    for i in range(N-K+1):
        ans = min(ans, abs(X[i]) + abs(X[i+K-1]-X[i]), abs(X[i+K-1]) + abs(X[i+K-1]-X[i]))
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans, abs(x[i])+abs(x[i]-x[i+K-1]))
        ans = min(ans, abs(x[i+K-1])+abs(x[i]-x[i+K-1]))
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))

    ans = 10**18
    for i in range(N-K+1):
        ans = min(ans, x[i+K-1] - x[i] + min(abs(x[i+K-1]), abs(x[i])))

    print(ans)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10**10
    for i in range(N-K+1):
        if X[i] < 0:
            if X[i+K-1] < 0:
                ans = min(ans, abs(X[i+K-1]))
            else:
                ans = min(ans, abs(X[i+K-1]) + abs(X[i]))
        else:
            ans = min(ans, abs(X[i]))
    print(ans)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = float("inf")
    for i in range(N-K+1):
        ans = min(ans, A[i+K-1] - A[i] + min(abs(A[i+K-1]), abs(A[i])))
    print(ans)

=======
Suggestion 10

def solve():
    N,K = map(int,input().split())
    X = list(map(int,input().split()))
    ans = float('inf')
    for i in range(N-K+1):
        ans = min(ans,min(abs(X[i]),abs(X[i+K-1]))+abs(X[i+K-1]-X[i]))
    print(ans)
    return 0
