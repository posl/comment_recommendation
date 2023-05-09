def main():
    H, W, N = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    # 重複を削除
    A = list(set(A))
    B = list(set(B))
    A.sort()
    B.sort()
    # 座標圧縮
    # 重複を削除した後の座標をキーとして、圧縮前の座標を値とする辞書を作成
    # 例えば、A = [1, 1, 3, 5, 5, 5, 7] のとき、A_dict = {1: 1, 3: 3, 5: 5, 7: 7} となる
    A_dict = {A[i]: i + 1 for i in range(len(A))}
    B_dict = {B[i]: i + 1 for i in range(len(B))}
    for i in range(N):
        print(A_dict[A[i]], B_dict[B[i]])
