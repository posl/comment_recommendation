def main():
    N = int(input())
    A = list(map(int, input().split()))
    # Aを反転させた配列を作成
    A_rev = A[::-1]
    # AとA_revの各要素を比較し、一致しない要素の数をカウント
    count = 0
    for i in range(N):
        if A[i] != A_rev[i]:
            count += 1
    # countが0の場合は、Aが回文なので0を出力
    if count == 0:
        print(0)
    # countが1の場合は、Aを1回操作するだけで回文にできるので1を出力
    elif count == 1:
        print(1)
    # countが2以上の場合は、Aを2回操作する必要があるので2を出力
    else:
        print(2)

if __name__ == '__main__':
    main()