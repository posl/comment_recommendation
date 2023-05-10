def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        _s, _t = input().split()
        s.append(_s)
        t.append(int(_t))
    # print(s)
    # print(t)
    # 1. オリジナルの提出を抽出
    # 2. 最高得点のオリジナル提出を抽出
    # 3. 最高得点のオリジナル提出の中で最も早い提出を抽出
    # 1. オリジナルの提出を抽出
    # 1-1. 最初の提出をオリジナル提出として追加
    # 1-2. 2回目以降の提出をオリジナル提出と比較する
    # 1-3. すでにオリジナル提出として追加済みの場合は、次の提出を比較する
    # 1-4. すでにオリジナル提出として追加済みでない場合は、オリジナル提出として追加する
    original = []
    for i in range(n):
        if i == 0:
            original.append([s[i], t[i]])
        else:
            is_original = True
            for j in range(len(original)):
                if s[i] == original[j][0]:
                    is_original = False
                    break
            if is_original:
                original.append([s[i], t[i]])
    # print(original)
    # 2. 最高得点のオリジナル提出を抽出
    # 2-1. オリジナル提出の中から最高得点を抽出
    # 2-2. 最高得点のオリジナル提出を抽出
    max_score = 0
    max_original = []
    for i in range(len(original)):
        if max_score < original[i][1]:
            max_score = original[i][1]
            max_original = []
            max

if __name__ == '__main__':
    main()