Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,k = map(int,input().split())
    x = list(map(int,input().split()))
    time = 0
    for i in range(k):
        if x[i] < 0:
            time += abs(x[i])
            if x[i+1] < 0:
                time += abs(x[i+1])
            else:
                time += x[i+1]
        else:
            time += x[i]
    print(time)

=======
Suggestion 2

def main():
    N,K = map(int,input().split())
    x = list(map(int,input().split()))

    min_time = 10**9
    for i in range(N-K+1):
        left = x[i]
        right = x[i+K-1]
        if left*right < 0:
            time = abs(left) + right - left
        else:
            time = max(abs(left),abs(right))
        if min_time > time:
            min_time = time
    print(min_time)

=======
Suggestion 3

def main():
    N,K = map(int,input().split())
    X = list(map(int,input().split()))
    X.sort()
    ans = 10**9+1
    for i in range(N-K+1):
        if X[i]*X[i+K-1] <= 0:
            ans = min(ans,2*abs(X[i])+abs(X[i+K-1]))
        else:
            ans = min(ans,max(abs(X[i]),abs(X[i+K-1])))
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
        if left*right <= 0:
            ans = min(ans, min(abs(left), abs(right))*2 + max(abs(left), abs(right)))
        else:
            ans = min(ans, max(abs(left), abs(right)))
    print(ans)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10**9

    for i in range(n-k+1):
        if x[i] <= 0 and x[i+k-1] >= 0:
            ans = min(ans, -x[i] + x[i+k-1] + min(-x[i], x[i+k-1]))

        elif x[i] <= 0:
            ans = min(ans, -x[i])

        else:
            ans = min(ans, x[i+k-1])

    print(ans)

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = float('inf')
    for i in range(N-K+1):
        left = X[i]
        right = X[i+K-1]
        if left * right <= 0:
            ans = min(ans, min(abs(left), abs(right)) * 2 + max(abs(left), abs(right)))
        else:
            ans = min(ans, max(abs(left), abs(right)))
    print(ans)

=======
Suggestion 8

def solve():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = float("inf")
    for i in range(N - K + 1):
        left = X[i]
        right = X[i + K - 1]
        ans = min(ans, min(abs(left) + abs(left - right), abs(right) + abs(left - right)))
    print(ans)

=======
Suggestion 9

def solve():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    #print(N, K, X)
    res = 10**9
    for i in range(N-K+1):
        #print(i, i+K-1)
        res = min(res, X[i+K-1]-X[i]+min(abs(X[i]), abs(X[i+K-1])))
    print(res)

=======
Suggestion 10

def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10 ** 8
    for i in range(n - k + 1):
        l = x[i]
        r = x[i + k - 1]
        if l * r <= 0:
            ans = min(ans, min(abs(l), abs(r)) * 2 + max(abs(l), abs(r)))
        else:
            ans = min(ans, max(abs(l), abs(r)))
    print(ans)
