def main():
    n = int(input())
    a = list(map(int, input().split()))
    # トーナメント表を作成
    # 配列の要素数は 2^N
    # 配列の要素番号は 0 から 2^N - 1
    # 配列の要素番号を 2 進数で表現したときの桁数は N
    # 配列の要素番号を 2 進数で表現したときの桁数が 1 であれば、その要素番号は葉ノード
    # 葉ノードの要素番号は 1 から 2^N までの整数を 2 進数で表現したときの桁数が 1 の桁である
    # 葉ノードの要素番号を 2 進数で表現したときの桁数が 1 である桁の値は、
    # その要素番号を 1 から 2^N までの整数を 2 進数で表現したときの桁数が 1 の桁の値と同じ
    # 例えば、要素番号が 2 の要素は、2 進数で表現したときの桁数が 1 である桁の値は 2 となる
    # 葉ノードの要素番号を 2 進数で表現したときの桁数が 1 である桁の値は、
    # その要素番号を 1 から 2^N までの整数を 2 進数で表現したときの桁数が 1 の桁の値と同じ
    # 例えば、要素番号が 2 の要素は、2 進数で表現したときの桁数が 1

if __name__ == '__main__':
    main()