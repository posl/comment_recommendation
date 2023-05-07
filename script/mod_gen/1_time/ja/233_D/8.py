def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # 連続部分列の和を求める
    # 例えば、A=[8,-3,5,7,0,-4] の場合
    # S=[8,5,10,17,17,13] となる
    # これは、A[0:2]の和、A[0:3]の和、A[0:4]の和、... となる
    S = [0]
    for i in range(N):
        S.append(S[-1]+A[i])
    # 連続部分列の和がKになる組み合わせを求める
    # 例えば、S=[8,5,10,17,17,13] で K=5 の場合
    # 8,5,10 と 5,10,17 の組み合わせがある
    # これは、S[0:3]とS[1:4]の和がKになることを意味する
    # これを、辞書型で管理する
    # 辞書のキーは連続部分列の和で、値はその和が出現する回数
    # 例えば、S=[8,5,10,17,17,13] で K=5 の場合
    # 8,5,10 の組み合わせは 1 組
    # 5,10,17 の組み合わせは 2 組
    # となるので、辞書は
    # {8:1, 5:1, 10:1, 17:2} となる
    # これを用いて、S[0:3]とS[1:4]の和がKになるか判定する
    # S[0:3] = 8+5+10 = 23
    # S[1:4] = 5+10+17

if __name__ == '__main__':
    main()