def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if len(s1) > 10 or len(s1) < 1:
        return
    if len(s2) > 10 or len(s2) < 1:
        return
    if len(s3) > 10 or len(s3) < 1:
        return
    if not s1.islower():
        return
    if not s2.islower():
        return
    if not s3.islower():
        return
    # 文字列の重複を削除して、文字列の長さが10を超えるならFalse
    if len(set(s1)) > 10:
        return
    if len(set(s2)) > 10:
        return
    if len(set(s3)) > 10:
        return
    # 文字列の長さが10を超えるならFalse
    if len(s1) > 10:
        return
    if len(s2) > 10:
        return
    if len(s3) > 10:
        return
    # 文字列の長さが1の場合
    if len(s1) == 1:
        if len(s2) == 1:
            if len(s3) == 1:
                if s1 == s2 and s1 == s3:
                    print('1')
                    print('1')
                    print('2')
                    return
                else:
                    print('UNSOLVABLE')
                    return
            else:
                print('UNSOLVABLE')
                return
        else:
            print('UNSOLVABLE')
            return
    else:
        # 文字列の長さが2以上の場合
        # 文字列の先頭が0の場合
        if s1[0] == '0' or s2[0] == '0' or s3[0] == '0':
            print('UNSOLVABLE')
            return
        else:
            # 文字列の長さが3以上の場合
            # 文字列の長さが3の場合
            if len(s1) == 3:
                if len(s2) == 3:
                    if len
