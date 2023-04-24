Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,k = map(int,input().split())
    x = list(map(int,input().split()))
    ans = 10**9
    for i in range(n-k+1):
        if x[i]*x[i+k-1]>=0:
            ans = min(ans,max(abs(x[i]),abs(x[i+k-1])))
        else:
            ans = min(ans,x[i+k-1]-x[i]+min(abs(x[i]),abs(x[i+k-1])))
    print(ans)
main()

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))

    ans = float('inf')
    for i in range(N - K + 1):
        left = X[i]
        right = X[i + K - 1]
        ans = min(ans, right - left + min(abs(left), abs(right)))
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = float("inf")
    for i in range(N - K + 1):
        left = X[i]
        right = X[i + K - 1]
        ans = min(ans, right - left + min(abs(left), abs(right)))
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans, min(abs(X[i+K-1]-X[i])+abs(X[i]), abs(X[i+K-1]-X[i])+abs(X[i+K-1])))
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans, min(abs(x[i])+abs(x[i+K-1]-x[i]), abs(x[i+K-1])+abs(x[i+K-1]-x[i])))
    print(ans)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    ans = float("inf")
    for i in range(n-k+1):
        ans = min(ans, x[i+k-1]-x[i]+min(abs(x[i]), abs(x[i+k-1])))
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10 ** 9
    for i in range(N - K + 1):
        l = X[i]
        r = X[i + K - 1]
        ans = min(ans, min(abs(l) + abs(l - r), abs(r) + abs(l - r)))
    print(ans)

main()

=======
Suggestion 8

def solve():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans, min(abs(x[i])+abs(x[i+K-1]-x[i]), abs(x[i+K-1])+abs(x[i+K-1]-x[i])))
    print(ans)
solve()

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))

    time = 10**9

    for i in range(N-K+1):
        if x[i+K-1] < 0:
            t = abs(x[i])
        elif x[i] > 0:
            t = x[i+K-1]
        else:
            t = 2*x[i+K-1] + abs(x[i])
        if t < time:
            time = t

    print(time)

=======
Suggestion 10

def main():
    #input
    N, K = map(int, input().split())
    X = list(map(int, input().split()))

    #compute
    if K == 1:
        print(0)
    else:
        ans = 10**9
        for i in range(N-K+1):
            left = X[i]
            right = X[i+K-1]
            if left*right <= 0:
                ans = min(ans, abs(left)+abs(right)+min(abs(left), abs(right)))
            else:
                ans = min(ans, max(abs(left), abs(right)))
        print(ans)
