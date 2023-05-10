def main():
    A, B = map(int, input().split())
    if A == 1:
        print(1)
        return
    # 二分探索
    # 1回目の操作でgを1増やすと、落下時間はA/((g+1)^(1/2))となる
    # 2回目の操作でgを1増やすと、落下時間はA/((g+2)^(1/2))となる
    # となるので、落下時間の増加は減少していく
    # 二分探索で、落下時間がBを超える最小の回数を求める
    # その回数-1が答え
    left = 0
    right = 10**18
    while left < right:
        mid = (left + right) // 2
        if A / ((mid + 1)**0.5) - A / ((mid + 2)**0.5) > B:
            left = mid + 1
        else:
            right = mid
    print(left - 1)

if __name__ == '__main__':
    main()