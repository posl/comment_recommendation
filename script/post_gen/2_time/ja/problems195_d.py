Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = [0] * M
    for i in range(M):
        X[i] = int(input())
    for i in range(Q):
        L, R = map(int, input().split())
        X_new = X[:L-1] + X[R:]
        X_new.sort(reverse=True)
        W_new = W[:]
        V_new = V[:]
        ans = 0
        for j in range(len(X_new)):
            for k in range(len(W_new)):
                if W_new[k] <= X_new[j]:
                    ans += V_new[k]
                    W_new[k] = 10**6 + 1
                    break
        print(ans)

=======
Suggestion 2

def main():
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = [0] * M
    for i in range(M):
        X[i] = int(input())
    for i in range(Q):
        L, R = map(int, input().split())
        L -= 1
        R -= 1
        box = X[:L] + X[R+1:]
        box.sort()
        W_sort = sorted(W)
        V_sort = sorted(V)
        print(box)
        print(W_sort)
        print(V_sort)
        #boxの大きさがW_sort[i]以下のものについて、V_sort[i]の価値の和を求める。
        #その中で、最大のものを出力する。
        #boxの大きさがW_sort[i]以下のものは、box内の要素がW_sort[i]以下のものの中で、最大のものを選ぶ。
        #boxの大きさがW_sort[i]以下のものは、box内の要素がW_sort[i]以下のものの中で、最大のものを選ぶ。
        #boxの大きさがW_sort[i]以下のものは、box内の要素がW_sort[i]以下のものの中で、最大のものを選ぶ。
        #boxの大きさがW_sort[i]以下のものは、box内の要素がW_sort[i]以下のものの中で、最大のものを選ぶ。
        #boxの大きさがW_sort[i]以下のものは、box内の要素がW_sort[i]以下のものの中で、最大のものを選ぶ。
        #boxの大きさがW_sort[i]以下のものは、box内の要素がW_sort[i]以下のものの中で、最大のものを選ぶ。
        #boxの大きさがW_sort

=======
Suggestion 3

def main():
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = [0] * M
    for i in range(M):
        X[i] = int(input())
    for i in range(Q):
        L, R = map(int, input().split())
        # 1. 箱の大きさを小さい順に並び替える
        # 2. 箱の大きさが小さい順に荷物を入れていく
        # 3. 箱の大きさが最大の箱から順に入れていく
        # 4. 箱の大きさが最大の箱から順に入れていく
        # 5. 箱の大きさが最大の箱から順に入れていく
        # 6. 箱の大きさが最大の箱から順に入れていく
        # 7. 箱の大きさが最大の箱から順に入れていく
        # 8. 箱の大きさが最大の箱から順に入れていく
        # 9. 箱の大きさが最大の箱から順に入れていく
        # 10. 箱の大きさが最大の箱から順に入れていく
        # 11. 箱の大きさが最大の箱から順に入れていく
        # 12. 箱の大きさが最大の箱から順に入れていく
        # 13. 箱の大きさが最大の箱から順に入れていく
        # 14. 箱の大きさが最大の箱から順に入れていく
        # 15. 箱の大きさが最大の箱から順に入

=======
Suggestion 4

def solve():
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = [0] * M
    for i in range(M):
        X[i] = int(input())
    for i in range(Q):
        L, R = map(int, input().split())
        #print(L, R)
        #print(W)
        #print(V)
        #print(X)
        #print()
        X_ = X[:L-1] + X[R:]
        #print(X_)
        dp = [0] * (sum(X_) + 1)
        for i in range(N):
            for j in range(sum(X_), W[i]-1, -1):
                dp[j] = max(dp[j], dp[j-W[i]] + V[i])
        print(dp[-1])

solve()

=======
Suggestion 5

def main():
    N, M, Q = map(int, input().split())
    wv = [list(map(int, input().split())) for _ in range(N)]
    X = list(map(int, input().split()))
    query = [list(map(int, input().split())) for _ in range(Q)]

    for L, R in query:
        box = X[:L - 1] + X[R:]
        box.sort()
        wv.sort(key=lambda x: x[1], reverse=True)
        ans = 0
        for w, v in wv:
            for i in range(len(box)):
                if box[i] >= w:
                    ans += v
                    box[i] = 0
                    break
        print(ans)

=======
Suggestion 6

def main():
    N, M, Q = map(int, input().split())
    wv = [tuple(map(int, input().split())) for _ in range(N)]
    X = list(map(int, input().split()))
    for _ in range(Q):
        L, R = map(int, input().split())
        x = X[:L - 1] + X[R:]
        x.sort()
        wv.sort(key=lambda x: x[1], reverse=True)
        ans = 0
        for wi, vi in wv:
            for i, xi in enumerate(x):
                if xi >= wi:
                    ans += vi
                    x[i] = -1
                    break
        print(ans)

=======
Suggestion 7

def main():
    N,M,Q = map(int,input().split())
    W = [0 for i in range(N)]
    V = [0 for i in range(N)]
    X = [0 for i in range(M)]
    for i in range(N):
        W[i],V[i] = map(int,input().split())
    for i in range(M):
        X[i] = int(input())
    for i in range(Q):
        L,R = map(int,input().split())
        #print(L,R)
        X_ = X[:L-1] + X[R:]
        #print(X_)
        dp = [[0 for i in range(sum(X_)+1)] for j in range(N+1)]
        for i in range(N):
            for j in range(sum(X_)+1):
                if j < W[i]:
                    dp[i+1][j] = dp[i][j]
                else:
                    dp[i+1][j] = max(dp[i][j],dp[i][j-W[i]]+V[i])
        print(dp[N][sum(X_)])

=======
Suggestion 8

def solve():
    N, M, Q = map(int, input().split())
    wv = [list(map(int, input().split())) for _ in range(N)]
    X = list(map(int, input().split()))
    LR = [list(map(int, input().split())) for _ in range(Q)]
    for l, r in LR:
        x = X[:l - 1] + X[r:]
        x.sort()
        wv.sort(key=lambda x: x[1], reverse=True)
        ans = 0
        for w, v in wv:
            for i in range(len(x)):
                if x[i] >= w:
                    ans += v
                    x[i] = 0
                    break
        print(ans)

solve()

=======
Suggestion 9

def knapsack(N, W, V, X):
    dp = [[0]*(X+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(X+1):
            if j < W[i]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j], dp[i][j-W[i]]+V[i])
    return dp[N][X]

=======
Suggestion 10

def solve(N, M, Q, W, V, X, Query):
    """
    N: 荷物の数
    M: 箱の数
    Q: クエリの数
    W: 荷物の重さ
    V: 荷物の価値
    X: 箱の大きさ
    Query: クエリ
    """
    # 箱の大きさの昇順にソート
    X.sort()
    # 荷物の価値の降順にソート
    # 価値の同じ荷物がある場合は重さの昇順にソート
    W_V = [(w, v) for w, v in zip(W, V)]
    W_V.sort(key=lambda x: (x[1], x[0]), reverse=True)
    # 答えを格納するリスト
    ans = []
    for l, r in Query:
        # 箱の大きさが l 番目から r 番目までの箱の中に入る荷物の価値の合計を求める
        # 箱の大きさの昇順にソートされているため、箱の大きさを二分探索で求める
        # 箱の大きさが X[i] 以下の荷物の価値の合計を求める
        # 価値の降順にソートされているため、価値の大きい荷物から順に箱に入れていく
        # 価値の大きい荷物から順に箱に入れていくため、二分探索を用いる
        # 二分探索の対象のリストは、箱の大きさが X[i] 以下の荷物の価値のリストとする
        # 二分探索の対象のリストの中の値は、箱の大きさが X[i]
