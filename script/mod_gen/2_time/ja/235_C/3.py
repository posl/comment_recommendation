def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * Q
    K = [0] * Q
    for i in range(Q):
        X[i], K[i] = map(int, input().split())
    # 前処理
    # 1. Aの各要素について、その要素がAの中で何回目に出現するかを計算
    # 2. 1.の結果を元に、Aの各要素の出現位置を記録
    # 3. 2.の結果を元に、Aの各要素の出現位置を累積和に変換
    # 4. 3.の結果を元に、Aの各要素の出現位置の累積和の累積和を計算
    # 5. 4.の結果を元に、Aの各要素の出現位置の累積和の累積和を累積和に変換
    # 1. Aの各要素について、その要素がAの中で何回目に出現するかを計算
    A_cnt = [0] * N
    for i in range(N):
        A_cnt[i] = A[:i].count(A[i]) + 1
    # 2. 1.の結果を元に、Aの各要素の出現位置を記録
    A_pos = [[] for _ in range(N)]
    for i in range(N):
        A_pos[i] = [j for j in range(N) if A[j] == A[i]]
    # 3. 2.の結果を元に、Aの各要素の出現位置を累積和に変換
    A_pos_cumsum = [[] for _ in range(N)]
    for i in range(N):
        A_pos_cumsum[i] = [0]
        for j in range(1, len(A

if __name__ == '__main__':
    main()