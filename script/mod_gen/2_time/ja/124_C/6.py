def main():
    s = input()
    # 0と1の数をカウント
    cnt0 = s.count('0')
    cnt1 = s.count('1')
    # 0と1の数を比較し、少ない方が答え
    if cnt0 < cnt1:
        print(cnt0)
    else:
        print(cnt1)

if __name__ == '__main__':
    main()