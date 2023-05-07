def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    for i in range(Q):
        X.append(int(input()))
    # Aの要素とXの要素を比較する
    # Aの要素がXの要素より大きい場合は、Aの要素をXの要素にするためには、Aの要素からXの要素を引く必要があるので、Aの要素からXの要素を引いた値を、Xの要素として配列に格納する
    # Aの要素がXの要素より小さい場合は、Aの要素をXの要素にするためには、Aの要素にXの要素を足す必要があるので、Xの要素からAの要素を引いた値を、Xの要素として配列に格納する
    for i in range(N):
        if A[i] > X[0]:
            X[0] = A[i] - X[0]
        else:
            X[0] = X[0] - A[i]
    # Xの要素の最小値を求める
    min_X = min(X)
    # Xの要素の最小値が0の場合は、Xの要素の最小値を出力する
    if min_X == 0:
        for i in range(Q):
            print(X[i])
    # Xの要素の最小値が0以外の場合は、Xの要素の最小値がXの要素の最大公約数となる
    else:
        # Xの要素の最大公約数を求める
        for i in range(Q):
            min_X = gcd(min_X, X[i])
        # Xの要素の最大公約数が0の場合は、Xの要素の最小値を出力する
        if min_X == 0:
            for i in range(Q):
                print(X[i])
        # Xの要

if __name__ == '__main__':
    main()