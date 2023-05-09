def main():
    S = input()
    N = len(S)
    # 0 と 1 の数を数える
    count_0 = S.count("0")
    count_1 = N - count_0
    # 0 と 1 の数を比較して、少ない方を塗り替える
    print(min(count_0, count_1))

if __name__ == '__main__':
    main()