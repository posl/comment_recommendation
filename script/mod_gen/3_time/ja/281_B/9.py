def main():
    s = input()
    # 1文字目が大文字でない場合
    if s[0].isupper() == False:
        print('No')
        return
    # 6文字目が大文字でない場合
    if s[6].isupper() == False:
        print('No')
        return
    # 2文字目〜5文字目が数字でない場合
    if s[1:6].isdigit() == False:
        print('No')
        return
    # 2文字目〜5文字目が100000以上999999以下の整数でない場合
    if int(s[1:6]) < 100000 or int(s[1:6]) > 999999:
        print('No')
        return
    print('Yes')

if __name__ == '__main__':
    main()