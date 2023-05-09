def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    # 都市 1 から都市 N へ移動することが出来ない場合は 0 と出力せよ。
    if 1 not in A or N not in B:
        print(0)
        return
    # 都市 1 から都市 N へ移動することが出来ない場合は 0 と出力せよ。
    if 1 not in B or N not in A:
        print(0)
        return
    # 都市 1 から都市 N へ移動することが出来ない場合は 0 と出力せよ。
    if 1 not in A and N not in B:
        print(0)
        return
    # 都市 1 から都市 N へ移動することが出来ない場合は 0 と出力せよ。
    if 1 not in B and N not in A:
        print(0)
        return
    # 都市 1 から都市 N へ移動することが出来ない場合は 0 と出力せよ。
    if 1 not in A and N not in A:
        print(0)
        return
    # 都市 1 から都市 N へ移動することが出来ない場合は 0 と出力せよ。
    if 1 not in B and N not in B:
        print(0)
        return
    # 都市 1 から都市 N へ移動することが出来る場合は 1 と出力せよ。
    if 1 in A and N in B:
        print(1)
        return
    # 都市 1 から都市 N へ移動することが出来る場合は 1 と出力せよ。
    if 1 in B and

if __name__ == '__main__':
    main()