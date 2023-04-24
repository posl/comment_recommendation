Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10 ** 9
    for i in range(N - K + 1):
        ans = min(ans, X[i + K - 1] - X[i] + min(abs(X[i]), abs(X[i + K - 1])))
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans, x[i+K-1]-x[i]+min(abs(x[i+K-1]), abs(x[i])))
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans, abs(X[i])+abs(X[i+K-1]-X[i]), abs(X[i+K-1])+abs(X[i+K-1]-X[i]))
    print(ans)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10**18
    for i in range(n-k+1):
        ans = min(ans, x[i+k-1]-x[i]+min(abs(x[i]), abs(x[i+k-1])))
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    ans = float('inf')
    for i in range(N-K+1):
        left = x[i]
        right = x[i+K-1]
        ans = min(ans, abs(left) + abs(left - right), abs(right) + abs(left - right))
    print(ans)

=======
Suggestion 6

def main():
    # input
    N, K = map(int, input().split())
    xs = list(map(int, input().split()))

    # compute
    """WRITE BELOW"""

    # output
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans, X[i+K-1]-X[i]+min(abs(X[i]), abs(X[i+K-1])))
    print(ans)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    if N == K:
        print(0)
        return
    if K == 1:
        print(min(abs(X[0]), abs(X[-1])))
        return

    # 絶対値の小さい順にソート
    X.sort(key=lambda x: abs(x))

    # 左端と右端のろうそくを除いた、残りのろうそくの絶対値の和
    # これを最小化する
    # 左端と右端のろうそくは、どちらかを選べば良いので、
    # それぞれの絶対値の和を計算する
    # 左端のろうそくの絶対値の和
    left = sum(map(abs, X[:K - 1]))
    # 右端のろうそくの絶対値の和
    right = sum(map(abs, X[-(K - 1):]))

    # 左端のろうそくの絶対値の和と右端のろうそくの絶対値の和の最小値
    print(min(left, right))

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10**10
    # N-K+1 個の区間について考える
    for i in range(N-K+1):
        # 区間の左端のろうそくに火を付けるときの最小の時間
        left = abs(X[i]) + abs(X[i]-X[i+K-1])
        # 区間の右端のろうそくに火を付けるときの最小の時間
        right = abs(X[i+K-1]) + abs(X[i]-X[i+K-1])
        # どちらかの時間が最小のものを答えにする
        ans = min(ans, left, right)
    print(ans)
