def main():
    N = int(input())
    # 1の位置を抜き出す
    one_positions = []
    for i in range(60):
        if N & (1 << i):
            one_positions.append(i)
    # 1の位置の数
    one_positions_count = len(one_positions)
    # 1の位置の数が15個を超える場合は処理を打ち切る
    if one_positions_count > 15:
        return
    # 1の位置の数だけループ
    for i in range(1 << one_positions_count):
        # 1の位置の数だけループ
        # 1の位置の数だけビットシフト
        # 1の位置の数だけビットシフトした値を足し合わせる
        x = 0
        for j in range(one_positions_count):
            if i & (1 << j):
                x += 1 << one_positions[j]
        print(x)

if __name__ == '__main__':
    main()