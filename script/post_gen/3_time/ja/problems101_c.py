Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[A[i] - 1] = i + 1

    ans = 0
    for i in range(N):
        if B[i] > K:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    ans = 0
    for i in range(n-k+1):
        ans += a[i+k-1] - a[i]
    print(ans)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-k+1):
        if a[i] != ans:
            ans += 1
        else:
            ans = 1
    print(ans)

=======
Suggestion 4

def main():
    # 入力
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # 連続するK個の要素を選んで、最小値で置き換える
    # これを繰り返すことで、この数列の要素をすべて等しくしたい
    # この操作を何回繰り返せば良いか
    # この問題の制約の下、このようなことは必ず可能であることが証明できる
    # 必要な操作の回数の最小値を求める
    # 連続するK個の要素を選んで、最小値で置き換えることを考える
    # 1回目の操作で、最小値を求める
    # 2回目の操作で、最小値を求める
    # ...
    # N-K+1回目の操作で、最小値を求める
    # これらの最小値を求める操作を繰り返す
    # これらの最小値の最大値を求める
    
    # 1回目の操作で、最小値を求める
    # 2回目の操作で、最小値を求める
    # ...
    # N-K+1回目の操作で、最小値を求める
    # これらの最小値を求める操作を繰り返す
    # これらの最小値の最大値を求める
    # 連続するK個の要素を選んで、最小値で置き換えることを考える
    # 1回目の操作で、最小値を求める
    # 2回目の操作で、最小値を求める
    #

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A

    # 連続したK個の要素を選ぶときに、選んだ要素の中の最小値で置き換える
    # 連続したK個の要素を選ぶときの総数はN-K+1通り
    # 連続したK個の要素の中の最小値は、K個の要素の中の最小値の中の最小値
    # すなわち、K個の要素の中の最小値を求める
    # K個の要素の中の最小値を求めるには、K個の要素を選ぶときの総数回の操作が必要
    # したがって、K個の要素を選ぶときの総数回の操作が必要
    print(N-K+1)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A

    # dp[i][j]: i番目までの要素で、j回操作したときの最小値
    dp = [[float('inf')] * (N+1) for _ in range(N+1)]

    # 初期化
    for i in range(1, N+1):
        dp[i][0] = A[i]

    # DP
    for i in range(1, N+1):
        for j in range(1, N+1):
            # 操作回数が要素数を超える場合は、前回の操作回数を継承
            if i - K < 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j])
            else:
                dp[i][j] = min(dp[i-1][j], dp[i-K][j-1])

    print(dp[N][N])

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # 最小値を求める
    minA = min(A)
    # 最小値を1にする
    for i in range(N):
        A[i] = A[i] - minA + 1
    # 1~Nまでの値をカウントするリストを作成
    B = [0 for i in range(N)]
    for i in range(N):
        B[A[i]-1] += 1
    # K個以上の値がある場合は、K個になるようにする
    for i in range(N):
        if B[i] >= K:
            B[i] = K
    # 1~Nまでの値をカウントするリストを作成
    C = [0 for i in range(N)]
    for i in range(N):
        C[A[i]-1] += 1
    # K個以上の値がある場合は、K個になるようにする
    for i in range(N):
        if C[i] >= K:
            C[i] = K
    # K個未満の値がある場合は、K個になるようにする
    for i in range(N):
        if C[i] < K:
            C[i] = 0
    # K個未満の値がある場合は、K個になるようにする
    for i in range(N):
        if C[i] < K:
            C[i] = 0
    # K個未満の値がある場合は、K個になるようにする
    for i in range(N):
        if C[i] < K:
            C[i] = 0
    # K個未満の値がある場合は、K個になるようにする
    for i in range(N):
        if C[i] < K:
            C[i] = 0
    # K個未満の値がある場合

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # Aの最大値を求める
    max_A = max(A)

    # Aの各要素が何回変更されるかを求める
    change = [0] * (max_A + 1)
    for i in range(N):
        change[A[i]] += 1

    # 変更回数の最大値を求める
    max_change = max(change)

    # 変更回数の最大値から操作回数を求める
    print(K - max_change)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A # 1-indexed

    # A[i] <= A[i+1] <= ... <= A[i+K-1] となるような i が存在するか
    def check(x):
        for i in range(1, N-K+2):
            if A[i] <= x <= A[i+K-1]:
                return True
        return False

    # 二分探索
    ok = 0
    ng = N + 1
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid

    # 答えは A[i] が ok になるまでの操作回数
    ans = 0
    for i in range(1, N-K+2):
        if A[i] <= ok <= A[i+K-1]:
            ans += ok - A[i]
        else:
            ans += A[i+K-1] - A[i]
    print(ans)

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # 1回目の操作で何個の要素を選ぶかを増やしていく
    # 2回目の操作で何個の要素を選ぶかを増やしていく
    # 3回目の操作で何個の要素を選ぶかを増やしていく
    # ...
    # というようにして，最終的にN個の要素を選ぶようにする
    # このとき，何回操作が必要かを求める
    # 1回目の操作で何個の要素を選ぶかは，K個ずつ増やしていく
    # 2回目の操作で何個の要素を選ぶかは，K-1個ずつ増やしていく
    # 3回目の操作で何個の要素を選ぶかは，K-2個ずつ増やしていく
    # ...
    # というようにして，最終的にK個ずつ増やしていく
    # このとき，何回操作が必要かは，(N-K+1)+(N-K+2)+...+(N-1)+N = (N-1)*N/2
    # つまり，N-1回操作が必要
    print(N-1)
