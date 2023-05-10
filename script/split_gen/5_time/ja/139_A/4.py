def main():
    # データ入力
    s = input()
    t = input()
    # 一致した数をカウントする
    count = 0
    for i in range(3):
        if s[i] == t[i]:
            count += 1
    # 結果を出力
    print(count)
