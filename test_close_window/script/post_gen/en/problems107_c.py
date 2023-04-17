Synthesizing 10/10 solutions

=======

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10**18
    for i in range(N-K+1):
        ans = min(ans, X[i+K-1]-X[i]+min(abs(X[i+K-1]),abs(X[i])))
    print(ans)

=======

def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10**9
    for i in range(n - k + 1):
        ans = min(ans, abs(x[i]) + abs(x[i + k - 1] - x[i]), abs(x[i + k - 1]) + abs(x[i + k - 1] - x[i]))
    print(ans)

=======

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10**18
    for i in range(N-K+1):
        ans = min(ans, abs(X[i])+abs(X[i]-X[i+K-1]), abs(X[i+K-1])+abs(X[i]-X[i+K-1]))
    print(ans)
main()

=======

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans, abs(X[i])+abs(X[i+K-1]-X[i]), abs(X[i+K-1])+abs(X[i+K-1]-X[i]))
    print(ans)

=======

def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans, abs(x[i])+abs(x[i+K-1]-x[i]), abs(x[i+K-1])+abs(x[i+K-1]-x[i]))
    print(ans)

=======

def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10**10
    for i in range(N-K+1):
        ans = min(ans, abs(x[i])+abs(x[i]-x[i+K-1]))
        ans = min(ans, abs(x[i+K-1])+abs(x[i]-x[i+K-1]))
    print(ans)

=======

def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10**18
    for i in range(N-K+1):
        left = x[i]
        right = x[i+K-1]
        ans = min(ans, abs(left) + abs(left-right), abs(right) + abs(left-right))
    print(ans)

=======

def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10 ** 9
    for i in range(N - K + 1):
        a = x[i]
        b = x[i + K - 1]
        if a >= 0:
            ans = min(ans, b)
        elif b <= 0:
            ans = min(ans, -a)
        else:
            ans = min(ans, 2 * b + a, 2 * -a + b)
    print(ans)

main()

=======

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    min_time = 10**18
    for i in range(N-K+1):
        min_time = min(min_time, abs(X[i])+abs(X[i+K-1]-X[i]), abs(X[i+K-1])+abs(X[i+K-1]-X[i]))
    print(min_time)

=======

def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))

    ans = float("inf")
    for i in range(N-K+1):
        #print(i, i+K-1)
        ans = min(ans, abs(x[i])+abs(x[i+K-1]-x[i]), abs(x[i+K-1])+abs(x[i+K-1]-x[i]))

    print(ans)
