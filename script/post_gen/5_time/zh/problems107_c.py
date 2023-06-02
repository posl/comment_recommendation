Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    if K == 1:
        print(0)
        return
    if K == N:
        print(X[-1] - X[0])
        return
    ans = 10**9
    for i in range(N-K+1):
        left = X[i]
        right = X[i+K-1]
        ans = min(ans, min(abs(left), abs(right)) + right - left)
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    if K == 1:
        print(0)
        return
    ans = 10 ** 9
    for i in range(N - K + 1):
        if X[i] * X[i + K - 1] < 0:
            ans = min(ans, min(abs(X[i]), abs(X[i + K - 1])) * 2 + max(abs(X[i]), abs(X[i + K - 1])))
        else:
            ans = min(ans, max(abs(X[i]), abs(X[i + K - 1])))
    print(ans)

=======
Suggestion 3

def main():
    pass

=======
Suggestion 4

def solve():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10 ** 9
    for i in range(n - k + 1):
        l = x[i]
        r = x[i + k - 1]
        if l * r < 0:
            ans = min(ans, min(-l, r) + r - l)
        else:
            ans = min(ans, max(l, r) - min(l, r))
    print(ans)

=======
Suggestion 5

def solve():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10**9
    for i in range(N-K+1):
        if X[i] <= 0 and X[i+K-1] >= 0:
            ans = min(ans, -X[i]*2 + X[i+K-1])
        elif X[i] <= 0 and X[i+K-1] <= 0:
            ans = min(ans, -X[i])
        elif X[i] >= 0 and X[i+K-1] >= 0:
            ans = min(ans, X[i+K-1])
    print(ans)
solve()

=======
Suggestion 6

def main():
    n,k = map(int,input().split())
    x = list(map(int,input().split()))
    #print(n,k)
    #print(x)
    ans = 10**9 + 1
    for i in range(n-k+1):
        left = x[i]
        right = x[i+k-1]
        time = min(abs(left),abs(right)) + right - left
        #print(left,right,time)
        ans = min(ans,time)
    print(ans)

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    # print(n, k, x)

    res = 10**8

    for i in range(n-k+1):
        if x[i] <= 0 and x[i+k-1] <= 0:
            res = min(res, abs(x[i]))
        elif x[i] >= 0 and x[i+k-1] >= 0:
            res = min(res, abs(x[i+k-1]))
        else:
            res = min(res, 2*min(abs(x[i]), abs(x[i+k-1])) + max(abs(x[i]), abs(x[i+k-1])))

    print(res)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10**9
    for i in range(N-K+1):
        if x[i]*x[i+K-1] <= 0:
            ans = min(ans, min(-x[i], x[i+K-1])*2+max(-x[i], x[i+K-1]))
        else:
            ans = min(ans, max(x[i], x[i+K-1]))
    print(ans)

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    ans = float('inf')
    for i in range(n - k + 1):
        l = x[i]
        r = x[i + k - 1]
        if l * r <= 0:
            ans = min(ans, min(abs(l), abs(r)) + r - l)
        else:
            ans = min(ans, max(abs(l), abs(r)))
    print(ans)
