def main():
    # 文字列の入力
    s = []
    for i in range(10):
        s.append(input())
    # print(s)
    # 1行目の文字列を基準にする
    # 1行目の文字列の中で最初に出現する#の位置をstartに保存する
    for i in range(10):
        if s[0][i] == '#':
            start = i
            break
    # print(start)
    # 1行目の文字列の中で最後に出現する#の位置をendに保存する
    for i in range(9, -1, -1):
        if s[0][i] == '#':
            end = i
            break
    # print(end)
    # 1行目の文字列の中の#の数を数えてcountに保存する
    count = 0
    for i in range(10):
        if s[0][i] == '#':
            count += 1
    # print(count)
    # 1行目の文字列の中の#の数が1個の場合
    if count == 1:
        print('1 1')
        print('1 1')
        exit()
    # 1行目の文字列の中の#の数が2個以上の場合
    # 1行目の文字列の中で最初に出現する#の位置と最後に出現する#の位置の差をdiffに保存する
    diff = end - start
    # print(diff)
    # 1行目の文字列の中の#の数が2個以上の場合
    # 1行目の文字列の中で最初に出現する#の位置と最後に出現する#の位置の差が1の場合
    if diff == 1:
        # 1行目の文字列の中で最初に出現する#の位置が1の場合
        if start == 1:
            # 1行目の文字列の中で最後に出現する#の位置が8の場合
            if end ==
