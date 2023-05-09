def main():
    # 標準入力から1行読み込み、整数に変換し、変数nに代入する
    n = int(input())
    # 標準入力から1行読み込み、スペース区切りでリストに変換し、変数aに代入する
    a = list(map(int, input().split()))
    # 重複を排除したリストをset_aに代入する
    set_a = set(a)
    # set_aの要素数を出力する
    print(len(set_a))
