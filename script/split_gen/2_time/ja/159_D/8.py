def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 1. Aの数字をカウント
    # 2. Aの数字のカウントの組み合わせを計算
    # 3. Aの数字のカウントの組み合わせから2を引く
    # 4. 3で0以下になったら0を出力
    # 5. 3で0より大きい数を出力
    # 1.
    A_count = [0] * (N + 1)
    for a in A:
        A_count[a] += 1
    # 2.
    A_count_combination = [0] * (N + 1)
    for a in A_count:
        A_count_combination[a] += 1
    # 3.
    A_count_combination = [a * (a - 1) // 2 for a in A_count_combination]
    # 4.
    A_count_combination = [a - 2 for a in A_count_combination]
    A_count_combination = [0 if a < 0 else a for a in A_count_combination]
    # 5.
    A_count_combination = [a * (N - 1) for a in A_count_combination]
    A_count_combination = [a // 2 for a in A_count_combination]
    for a in A_count_combination[1:]:
        print(a)
