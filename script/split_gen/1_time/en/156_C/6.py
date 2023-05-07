def main():
    # 1行目の入力
    N = int(input())
    # 2行目の入力
    X = [int(i) for i in input().split()]
    # 結果出力
    print(min([sum([(x - p) ** 2 for x in X]) for p in range(1, 101)]))
