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
