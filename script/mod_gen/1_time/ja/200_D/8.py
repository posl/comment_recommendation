def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 余りをキーとして、Aのインデックスを値とする辞書を作成
    # 余りが重複する場合は、インデックスを追加
    remainder = {}
    for i, a in enumerate(A):
        if a % 200 in remainder:
            remainder[a % 200].append(i)
        else:
            remainder[a % 200] = [i]
    # 余りが重複しているものがあれば、それを出力
    for r in remainder:
        if len(remainder[r]) > 1:
            print("Yes")
            print(1, remainder[r][0] + 1)
            print(1, remainder[r][1] + 1)
            exit()
    # 余りが重複していない場合
    # 余りの組み合わせを作成
    # 余りが重複している場合と同様に、インデックスを追加
    combinations = {}
    for r1 in remainder:
        for r2 in remainder:
            if r1 == r2:
                continue
            if (r1 + r2) % 200 in combinations:
                combinations[(r1 + r2) % 200].append([r1, r2])
            else:
                combinations[(r1 + r2) % 200] = [[r1, r2]]
    # 余りの組み合わせが重複しているものがあれば、それを出力
    for c in combinations:
        if len(combinations[c]) > 1:
            print("Yes")
            print(len(remainder[combinations[c][0][0]]), *list(map(lambda x: x + 1, remainder[combinations[c][0][0]])))
            print(len(remainder[combinations[c][0][1]]), *list(map(lambda x: x + 1, remainder[combinations[c][0][1]])))
            exit()
    # 余りの組み合わせが重複してい

if __name__ == '__main__':
    main()