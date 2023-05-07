def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    K = []
    for _ in range(Q):
        x, k = map(int, input().split())
        X.append(x)
        K.append(k)
    # A に含まれる数字の出現回数をカウント
    # A に含まれる数字の出現回数をカウント
    from collections import defaultdict
    d = defaultdict(int)
    for a in A:
        d[a] += 1
    # A の要素を前から順に見ていったときに、各数字の何回目に登場するかを記録
    # A の要素を前から順に見ていったときに、各数字の何回目に登場するかを記録
    d2 = defaultdict(list)
    for i, a in enumerate(A):
        d2[a].append(i)
    # 各クエリに対する答えを求める
    # 各クエリに対する答えを求める
    for x, k in zip(X, K):
        if d[x] < k:
            print(-1)
        else:
            print(d2[x][k-1] + 1)
