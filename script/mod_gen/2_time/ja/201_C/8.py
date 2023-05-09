def main():
    # 文字列を取得
    s = input()
    # 答えを格納する変数
    ans = 0
    # 0から9999までループ
    for i in range(10000):
        # 暗証番号を取得
        num = str(i).zfill(4)
        # 暗証番号に含まれる文字列をリストに格納
        li = list(num)
        # リストの要素をループ
        for j in range(4):
            # 暗証番号の文字列がsの文字列と一致しているか
            if s[int(li[j])] == "x":
                # 一致していない場合はループを抜ける
                break
        # リストの要素をループ
        else:
            # 暗証番号の文字列がsの文字列と一致しているか
            for k in range(10):
                # 暗証番号の文字列がsの文字列と一致しているか
                if s[k] == "o":
                    # 一致している場合
                    # 暗証番号の文字列がリストに含まれているか
                    if str(k) in li:
                        # 含まれている場合はループを抜ける
                        break
            # リストの要素をループ
            else:
                # 答えに1を加算
                ans += 1
    # 答えを出力
    print(ans)

if __name__ == '__main__':
    main()