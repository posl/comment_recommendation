def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    # Aの各要素の最小値を求める
    min_A = min([min(A[i]) for i in range(H)])
    # Aの各要素からmin_Aを引いた値をsum_Aに足していく
    sum_A = 0
    for i in range(H):
        for j in range(W):
            sum_A += A[i][j] - min_A
    print(sum_A)
