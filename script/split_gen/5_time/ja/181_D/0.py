def can_be_divided_by_8(s):
    if len(s) == 1:
        if int(s) % 8 == 0:
            return True
        else:
            return False
    elif len(s) == 2:
        if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
            return True
        else:
            return False
    else:
        # 3桁以上の場合
        # 3桁の場合
        for i in range(1,10):
            # 3桁の数値の中に、i があるかどうか
            if str(i) in s:
                # 3桁の数値の中に、i がある場合
                # 3桁の数値の中から、i を取り除く
                tmp = s.replace(str(i), "", 1)
                for j in range(1,10):
                    # 3桁の数値の中に、j があるかどうか
                    if str(j) in tmp:
                        # 3桁の数値の中に、j がある場合
                        # 3桁の数値の中から、j を取り除く
                        tmp2 = tmp.replace(str(j), "", 1)
                        if int(tmp2) % 8 == 0:
                            return True
        return False
s = input()
