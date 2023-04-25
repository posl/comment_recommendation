Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10**18
    for i in range(N-K+1):
        ans = min(ans, abs(X[i])+abs(X[i]-X[i+K-1]), abs(X[i+K-1])+abs(X[i]-X[i+K-1]))
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans, abs(X[i])+abs(X[i+K-1]-X[i]), abs(X[i+K-1])+abs(X[i]-X[i+K-1]))
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10**10
    for i in range(N-K+1):
        ans = min(ans, X[i+K-1]-X[i]+min(abs(X[i+K-1]), abs(X[i])))
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))

    ans = 10 ** 18
    for i in range(N - K + 1):
        ans = min(ans, X[i + K - 1] - X[i] + min(abs(X[i]), abs(X[i + K - 1])))
    print(ans)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    ans = float("inf")
    for i in range(n-k+1):
        ans = min(ans, min(abs(x[i]), abs(x[i+k-1])) + abs(x[i]-x[i+k-1]))
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10**9
    for i in range(N-K+1):
        a = x[i]
        b = x[i+K-1]
        if a >= 0:
            ans = min(ans, b)
        elif b <= 0:
            ans = min(ans, -a)
        else:
            ans = min(ans, min(abs(a)+b, abs(b)+a))
    print(ans)

=======
Suggestion 7

def main():
    N,K = map(int,input().split())
    x = list(map(int,input().split()))
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans, x[i+K-1] - x[i] + min(abs(x[i+K-1]),abs(x[i])))
    print(ans)

=======
Suggestion 8

def main():
    n, k = [int(x) for x in input().split()]
    x = [int(x) for x in input().split()]
    
    ans = 10**9
    for i in range(n-k+1):
        ans = min(ans, x[i+k-1] - x[i] + min(abs(x[i+k-1]), abs(x[i])))
    
    print(ans)

main()

This is a Python 3 solution.

The algorithm is as follows:

Sort the candles in ascending order.

Check the minimum time for each case where the starting point is in the range of the first candle to the last candle.

The minimum time is the minimum time of the following two:

The time required to move from the starting point to the rightmost candle, and then to the leftmost candle.

The time required to move from the starting point to the leftmost candle, and then to the rightmost candle.

The time required to move from the starting point to the rightmost candle, and then to the leftmost candle.

The time required to move from the starting point to the leftmost candle, and then to the rightmost candle.

The time required to move from the starting point to the leftmost candle, and then to the rightmost candle.

The time required to move from the starting point to the rightmost candle, and then to the leftmost candle.

The time required to move from the starting point to the rightmost candle, and then to the leftmost candle.

The time required to move from the starting point to the leftmost candle, and then to the rightmost candle.

The time required to move from the starting point to the leftmost candle, and then to the rightmost candle.

The time required to move from the starting point to the rightmost candle, and then to the leftmost candle.

The time required to move from the starting point to the rightmost candle, and then to the leftmost candle.

The time required to move from the starting point to the leftmost candle, and then to the rightmost candle.

The time required to move from the starting point to the rightmost candle, and then to the leftmost candle.

The time required to move from the starting point to the leftmost candle, and then to the rightmost candle.

The time required to move from the starting point to the leftmost candle, and then to the rightmost candle.

The time required to move from the starting point to the

=======
Suggestion 9

def solve(N,K,x):
    # write your code in Python 3.6
    ans = 10**20
    for i in range(N-K+1):
        ans = min(ans, abs(x[i])+abs(x[i+K-1]-x[i]), abs(x[i+K-1])+abs(x[i+K-1]-x[i]))
    return ans
