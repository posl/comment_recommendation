def main():
    n, m = map(int, input().split())
    s_c = [list(map(int, input().split())) for _ in range(m)]
    #print(n, m, s_c)
    #条件を満たす 0 以上の整数が存在すれば、それらのうち最小のものを出力してください。そのような整数が存在しなければ、 -1と出力してください。
    #十進表記で丁度 N 桁である。(0 は 1 桁の整数とする。その他の整数については、先頭に 0 をつけた表記は認めない。)
    #左から数えて s_i 桁目は c_i である。(i = 1, 2, ..., M)
    #N = 3
    #M = 3
    #s_c = [[1, 7], [3, 2], [1, 7]]
    #N = 3
    #M = 2
    #s_c = [[2, 1], [2, 3]]
    #N = 3
    #M = 1
    #s_c = [[1, 0]]
    #N = 3
    #M = 0
    #s_c = []
    #N = 1
    #M = 0
    #s_c = []
    #N = 1
    #M = 1
    #s_c = [[1, 7]]
    #N = 1
    #M = 2
    #s_c = [[1, 7], [1, 7]]
    #N = 1
    #M = 3
    #s_c = [[1, 7], [1, 7], [1, 7]]
    #N = 1
    #M = 4
    #s_c = [[1, 7], [1, 7], [1, 7], [1, 7]]
    #N = 1
    #M = 5
    #s_c = [[1, 7], [1, 7], [1

if __name__ == '__main__':
    main()