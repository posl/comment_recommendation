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

if __name__ == '__main__':
    main()