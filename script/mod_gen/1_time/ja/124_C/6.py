def main():
    S = input()
    # 0と1の数を数える
    c0 = S.count("0")
    c1 = S.count("1")
    # 0と1の数が少ない方を答えとする
    print(min(c0, c1))
main()

if __name__ == '__main__':
    main()