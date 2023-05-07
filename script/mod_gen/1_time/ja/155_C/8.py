def main():
    N = int(input())
    S = [input() for i in range(N)]
    # 各文字列の出現回数をカウント
    count = {}
    for s in S:
        if s in count:
            count[s] += 1
        else:
            count[s] = 1
    # 出現回数が最大の文字列を取得
    max_count = max(count.values())
    # 出現回数が最大の文字列を辞書順で出力
    for s in sorted(count.keys()):
        if count[s] == max_count:
            print(s)

if __name__ == '__main__':
    main()