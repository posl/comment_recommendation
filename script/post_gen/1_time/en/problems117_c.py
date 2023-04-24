Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    D = [X[i+1]-X[i] for i in range(M-1)]
    D.sort(reverse=True)
    print(sum(D[N-1:]))

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    diff = [x[i+1] - x[i] for i in range(m-1)]
    diff.sort()
    if m > n:
        print(sum(diff[:m-n]))
    else:
        print(0)

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    if n >= m:
        print(0)
        return
    d = []
    for i in range(m - 1):
        d.append(x[i + 1] - x[i])
    d.sort(reverse=True)
    ans = sum(d[n - 1:])
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    if N >= M:
        print(0)
        return
    d = []
    for i in range(M-1):
        d.append(X[i+1] - X[i])
    d.sort()
    print(sum(d[:M-N]))

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    if N >= M:
        print(0)
        return
    d = []
    for i in range(M-1):
        d.append(X[i+1] - X[i])
    d.sort(reverse=True)
    print(sum(d[N-1:]))

main()

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    if N >= M:
        print(0)
        return

    D = []
    for i in range(M-1):
        D.append(X[i+1] - X[i])
    D.sort()

    ans = sum(D[:M-N])
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    X = sorted(map(int, input().split()))
    if N >= M:
        print(0)
        return
    D = [0] * (M-1)
    for i in range(M-1):
        D[i] = X[i+1] - X[i]
    D.sort()
    print(sum(D[:M-N]))

=======
Suggestion 8

def main():
    from bisect import bisect_left, bisect_right
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    #print(X)
    ans = 0
    for i in range(M-1):
        ans += X[i+1] - X[i]
    #print(ans)
    for i in range(M-1):
        ans -= max(0, X[i+1] - X[i] - 1)
    #print(ans)
    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    if N >= M:
        print(0)
        return
    # X_i, X_i+1間の距離を求める
    d = [X[i+1] - X[i] for i in range(M-1)]
    d.sort(reverse=True)
    # 距離の大きい順にN-1個の距離を削除する
    for i in range(N-1):
        d.pop(0)
    print(sum(d))

=======
Suggestion 10

def main():
    #input
    N, M = map(int, input().split())
    Xs = list(map(int, input().split()))
    Xs.sort()

    #compute
    #dp[i][j] := i番目のピースをj番目のXsに移動させるまでの最小コスト
    dp = [[float('inf')] * M for _ in range(N)]
    for j in range(M):
        dp[0][j] = abs(Xs[j] - Xs[0])
    for i in range(1, N):
        for j in range(i, M):
            dp[i][j] = min(dp[i][j-1], dp[i-1][j-1] + abs(Xs[j] - Xs[j-i]))

    #output
    print(dp[-1][-1])
