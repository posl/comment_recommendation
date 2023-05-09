def main():
    N, K = map(int, input().split())
    if N >= K:
        print(1)
        return
    # 1. K-1 以下の出目について、サイコロを振った時の確率を求める
    # 2. K 以上の出目について、サイコロを振った時の確率を求める
    # 3. 1. と 2. を足す
    # 4. 3. を N で割る
    # 5. 4. を 1 から引く
    # 6. 5. を出力する
    # 1.
    sum1 = 0
    for i in range(1, K):
        sum1 += (1/N) * (1/2)**i
    # 2.
    sum2 = 0
    for i in range(K, N+1):
        sum2 += (1/N) * (1/2)**i
    # 3.
    sum3 = sum1 + sum2
    # 4.
    sum4 = sum3 / N
    # 5.
    sum5 = 1 - sum4
    # 6.
    print(sum5)

if __name__ == '__main__':
    main()