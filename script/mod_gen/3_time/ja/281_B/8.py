def main():
    s = input()
    # 1文字目
    if s[0].isupper():
        # 2文字目以降
        for i in range(1, len(s)):
            # 2文字目以降の1文字目
            if i == 1:
                if s[i].isnumeric():
                    continue
                else:
                    print('No')
                    return
            # 2文字目以降の2文字目以降
            else:
                if s[i].isupper():
                    continue
                else:
                    print('No')
                    return
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()