def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 採用された人の番号
    admission = []
    # 1. 最高点数の人をX人採用
    # 2. 1で採用されなかった人の中で最高点数の人をY人採用
    # 3. 2で採用されなかった人の中で最高点数の人をZ人採用
    # 1. 最高点数の人をX人採用
    for i in range(X):
        # 最高点数の人の番号を探す
        max_point = max(A)
        max_index = A.index(max_point)
        # 採用された人の番号に追加
        admission.append(max_index + 1)
        # 採用された人の点数を-1にして採用されていることを示す
        A[max_index] = -1
    # 2. 1で採用されなかった人の中で最高点数の人をY人採用
    for i in range(Y):
        # 最高点数の人の番号を探す
        max_point = max(B)
        max_index = B.index(max_point)
        # 採用された人の番号に追加
        admission.append(max_index + 1)
        # 採用された人の点数を-1にして採用されていることを示す
        B[max_index] = -1
    # 3. 2で採用されなかった人の中で最高点数の人をZ人採用
    for i in range(Z):
        # 最高点数の人の番号を探す
        max_point = max(A, B)
        max_index = A.index(max_point)
        # 採用された人の番号に追加
        admission.append(max_index + 1)
        # 採用され

if __name__ == '__main__':
    main()