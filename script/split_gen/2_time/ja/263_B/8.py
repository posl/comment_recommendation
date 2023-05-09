def main():
    # 標準入力の受け取り
    n = int(input())
    p_list = list(map(int, input().split()))
    # 人数分の配列を作成
    parent_list = [0] * n
    # 親の人数分ループ
    for i in range(n - 1):
        # 親の人数分ループ
        for j in range(n - 1):
            # 親の人数分ループ
            if p_list[j] == i + 2:
                # 親の人数分ループ
                parent_list[i + 1] = parent_list[i] + 1
    # 結果を出力
    print(parent_list[n - 1])
