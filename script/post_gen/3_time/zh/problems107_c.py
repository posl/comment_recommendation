Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10 ** 9
    for i in range(N - K + 1):
        l = X[i]
        r = X[i + K - 1]
        if l * r <= 0:
            ans = min(ans, min(abs(l), abs(r)) * 2 + max(abs(l), abs(r)))
        else:
            ans = min(ans, max(abs(l), abs(r)))
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10 ** 9
    for i in range(N - K + 1):
        l = x[i]
        r = x[i + K - 1]
        if l * r <= 0:
            ans = min(ans, min(abs(l), abs(r)) * 2 + max(abs(l), abs(r)))
        else:
            ans = min(ans, max(abs(l), abs(r)))
    print(ans)

main()

=======
Suggestion 3

def main():
    pass

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    time = 10**9
    for i in range(N-K+1):
        time = min(time, min(abs(x[i])+x[i+K-1]-x[i], abs(x[i+K-1])+x[i+K-1]-x[i]))
    print(time)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    if K == 1:
        print(0)
        return
    ans = 10 ** 8
    for i in range(N - K + 1):
        if x[i] <= 0 <= x[i + K - 1]:
            ans = min(ans, min(abs(x[i]), abs(x[i + K - 1])) * 2 + max(abs(x[i]), abs(x[i + K - 1])))
        else:
            ans = min(ans, max(abs(x[i]), abs(x[i + K - 1])))
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10 ** 9
    for i in range(N - K + 1):
        left = X[i]
        right = X[i + K - 1]
        ans = min(ans, min(abs(left) + abs(left - right), abs(right) + abs(left - right)))
    print(ans)

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    x = list(map(int,input().split()))
    ans = 10**9
    for i in range(n-k+1):
        left = x[i]
        right = x[i+k-1]
        ans = min(ans,min(abs(left),abs(right))+right-left)
    print(ans)

=======
Suggestion 8

def solve(n, k, xs):
    if k == 1:
        return 0
    if n == k:
        return xs[n - 1] - xs[0]
    res = 10 ** 9
    for i in range(0, n - k + 1):
        res = min(res, xs[i + k - 1] - xs[i] + min(abs(xs[i]), abs(xs[i + k - 1])))
    return res

=======
Suggestion 9

def solve():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10**9
    for i in range(n-k+1):
        l = x[i]
        r = x[i+k-1]
        if l <= 0 <= r:
            ans = min(ans, min(-l, r) * 2 + max(-l, r))
        else:
            ans = min(ans, max(-l, r))
    print(ans)

=======
Suggestion 10

def main():
    n,k = map(int,input().split())
    x = list(map(int,input().split()))
    x.sort()
    ans = 10**9
    for i in range(n-k+1):
        l = x[i]
        r = x[i+k-1]
        ans = min(ans,abs(l)+abs(r-l),abs(r)+abs(l-r))
    print(ans)
