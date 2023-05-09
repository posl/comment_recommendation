def main():
    from sys import stdin
    readline = stdin.readline
    N = int(readline())
    A = list(map(int, readline().split()))
    # 1度でも切ると360度の範囲になるので、
    # 360度で割った余りをとれば、360度に収まる。
    # また、360度を超えた場合は、360度を引けば、360度に収まる。
    # 0度から359度に変換する。
    A = [a % 360 for a in A]
    A = [a if a != 0 else 360 for a in A]
    # 360度の範囲に収まった角度のリストを作成する。
    # 0度から359度のリストを作成する。
    angles = [i for i in range(360)]
    # 360度の範囲に収まった角度のリストの中から、
    # 360度を超えた角度を除外する。
    # 0度から359度のリストの中から、
    # 360度を超えた角度を除外する。
    for a in A:
        angles.remove(a)
    # 360度の範囲に収まった角度のリストの中から、
    # 360度を超えた角度を除外する。
    # 0度から359度のリストの中から、
    # 360度を超えた角度を除外する。
    for a in A:
        angles.remove(a)
    # 360度の範囲に収まった角度のリストの中から、
    # 360度を超えた角度を除外する。
    for a in A:
        angles.remove(a)
    # 360度の範囲に収まった角度のリストの中から、
    # 360度を超えた角度を除外する。
    for a in A:
        angles.remove(a)
    # 360度の範囲に収

if __name__ == '__main__':
    main()