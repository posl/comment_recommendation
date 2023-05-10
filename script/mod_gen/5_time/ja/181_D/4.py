def main():
    s = input()
    if len(s) == 1:
        if s == "8":
            print("Yes")
        else:
            print("No")
    elif len(s) == 2:
        if int(s) % 8 == 0:
            print("Yes")
        else:
            s = s[::-1]
            if int(s) % 8 == 0:
                print("Yes")
            else:
                print("No")
    else:
        # 3桁以上の場合
        # すべての8の倍数をリストに格納
        l = []
        for i in range(1, 1000):
            if i % 8 == 0:
                l.append(i)
        # 各数字の個数を数える
        d = {}
        for i in range(10):
            d[str(i)] = 0
        for i in range(len(s)):
            d[s[i]] += 1
        # 8の倍数が作れるかどうか判定
        for i in range(len(l)):
            # 8の倍数の各桁の数字の個数を数える
            d_8 = {}
            for j in range(10):
                d_8[str(j)] = 0
            s_8 = str(l[i])
            for j in range(len(s_8)):
                d_8[s_8[j]] += 1
            # 8の倍数の各桁の数字の個数が、sの各桁の数字の個数以下なら、Yes
            f = True
            for j in range(10):
                if d_8[str(j)] > d[str(j)]:
                    f = False
            if f:
                print("Yes")
                exit()
        print("No")

if __name__ == '__main__':
    main()