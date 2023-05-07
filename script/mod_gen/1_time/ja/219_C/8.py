def main():
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    # アルファベット順を辞書型で作成
    alphabet_dict = {}
    for i, alphabet in enumerate(X):
        alphabet_dict[alphabet] = i
    # アルファベットの値を辞書型で作成
    value_dict = {}
    for i, value in enumerate(sorted(alphabet_dict.values())):
        value_dict[value] = i
    # アルファベットを数値に変換
    S = [[value_dict[alphabet_dict[alphabet]] for alphabet in s] for s in S]
    # 数値をアルファベットに変換
    S = [[X[value] for value in s] for s in S]
    # アルファベットを辞書順に並び替え
    S.sort()
    # 数値をアルファベットに変換
    S = [[X[value] for value in s] for s in S]
    # アルファベットを文字列に変換
    S = [''.join(s) for s in S]
    for s in S:
        print(s)

if __name__ == '__main__':
    main()