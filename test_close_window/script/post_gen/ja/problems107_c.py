Synthesizing 9/10 solutions (Duplicates hidden)

=======

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans, X[i+K-1]-X[i]+min(abs(X[i+K-1]), abs(X[i])))
    print(ans)

=======

def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10**18
    for i in range(N - K + 1):
        ans = min(ans, abs(x[i]) + abs(x[i] - x[i + K - 1]), abs(x[i + K - 1]) + abs(x[i] - x[i + K - 1]))
    print(ans)
main()

=======

def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))

    ans = 10 ** 9
    for i in range(N - K + 1):
        ans = min(ans, x[i + K - 1] - x[i] + min(abs(x[i]), abs(x[i + K - 1])))

    print(ans)

=======

def solve():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    ans = float('inf')
    for i in range(N - K + 1):
        ans = min(ans, x[i + K - 1] - x[i] + min(abs(x[i + K - 1]), abs(x[i])))
    print(ans)

=======

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10**20
    for i in range(N-K+1):
        ans = min(ans, X[i+K-1]-X[i]+min(abs(X[i+K-1]), abs(X[i])))
    print(ans)

=======

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    ans = 10**18
    for i in range(N-K+1):
        ans = min(ans, X[i+K-1]-X[i]+min(abs(X[i+K-1]),abs(X[i])))
    print(ans)

=======

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 100000000000000000000
    for i in range(N - K + 1):
        ans = min(ans, abs(X[i]) + abs(X[i] - X[i + K - 1]))
        ans = min(ans, abs(X[i + K - 1]) + abs(X[i] - X[i + K - 1]))
    print(ans)

=======

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))

    ans = 10**10

    for i in range(N-K+1):
        #print(X[i], X[i+K-1])
        ans = min(ans, min(abs(X[i]), abs(X[i+K-1]))+X[i+K-1]-X[i])

    print(ans)
