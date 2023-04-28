Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10**9
    for i in range(n-k+1):
        if x[i]*x[i+k-1] >= 0:
            ans = min(ans, max(abs(x[i]), abs(x[i+k-1])))
        else:
            ans = min(ans, 2*min(abs(x[i]), abs(x[i+k-1])) + max(abs(x[i]), abs(x[i+k-1])))
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10 ** 9
    for i in range(N - K + 1):
        if x[i] * x[i + K - 1] < 0:
            ans = min(ans, min(abs(x[i]), abs(x[i + K - 1])) + abs(x[i + K - 1]) - abs(x[i]))
        else:
            ans = min(ans, max(abs(x[i]), abs(x[i + K - 1])))
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans, min(abs(X[i+K-1]-X[i])+abs(X[i]), abs(X[i+K-1]-X[i])+abs(X[i+K-1])))
    print(ans)

=======
Suggestion 4

def solve():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10 ** 9
    for i in range(N - K + 1):
        l = X[i]
        r = X[i + K - 1]
        if l < 0 and r < 0:
            ans = min(ans, -l)
        elif l < 0 and r >= 0:
            ans = min(ans, -l + r + min(-l, r))
        else:
            ans = min(ans, r)
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10**9
    for i in range(N-K+1):
        r = X[i+K-1]
        l = X[i]
        ans = min(ans, r-l+min(abs(r), abs(l)))
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    min_time = 10 ** 10
    for i in range(N - K + 1):
        if X[i] < 0 and X[i + K - 1] < 0:
            time = -X[i]
        elif X[i] > 0 and X[i + K - 1] > 0:
            time = X[i + K - 1]
        else:
            time = min(-X[i] * 2 + X[i + K - 1], X[i + K - 1] * 2 - X[i])
        if time < min_time:
            min_time = time
    print(min_time)

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    x = sorted(x)
    ans = 10 ** 9
    for i in range(n - k + 1):
        ans = min(ans, x[i + k - 1] - x[i] + min(abs(x[i]), abs(x[i + k - 1])))
    print(ans)

=======
Suggestion 8

def main():
    n,k = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10**10
    for i in range(n-k+1):
        ans = min(ans, abs(x[i])+abs(x[i]-x[i+k-1]))
        ans = min(ans, abs(x[i+k-1])+abs(x[i]-x[i+k-1]))
    print(ans)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    min_time = 10 ** 9
    for i in range(N - K + 1):
        right = X[i + K - 1]
        if X[i] < 0 and right < 0:
            time = -X[i]
        elif X[i] > 0 and right > 0:
            time = right
        else:
            time = min(abs(X[i]), abs(right)) * 2 + max(abs(X[i]), abs(right))
        min_time = min(min_time, time)
    print(min_time)
main()

=======
Suggestion 10

def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    total = 10**9
    for i in range(n - k + 1):
        left = x[i]
        right = x[i + k - 1]
        if left < 0 and right < 0:
            total = min(total, -left)
        elif left < 0 and right >= 0:
            total = min(total, -left + right + min(-left, right))
        else:
            total = min(total, right)
    print(total)
