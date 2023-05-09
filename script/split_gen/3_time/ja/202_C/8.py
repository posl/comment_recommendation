def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    # Bを要素番号とするリストを作成
    B_list = [0] * (N + 1)
    for i in range(N):
        B_list[B[i]] = i
    # Cの各要素をBの要素番号に変換
    C_list = [0] * N
    for i in range(N):
        C_list[i] = B_list[C[i]]
    # C_listをソート
    C_list.sort()
    # Aの各要素の値をBの要素番号に変換
    A_list = [0] * N
    for i in range(N):
        A_list[i] = B_list[A[i]]
    # A_listをソート
    A_list.sort()
    # A_listとC_listの各要素を比較して、条件を満たす組の数をカウント
    count = 0
    for i in range(N):
        # A_listの要素以上の値を持つ最初のC_listの要素のインデックスを取得
        index = binary_search(C_list, A_list[i])
        # A_listの要素がC_listに含まれている場合
        if index != -1:
            count += N - index
    print(count)
