def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # 青色のマスの位置を取得
    blue = [0] * (N + 1)
    for i in range(M):
        blue[A[i]] = 1
    # 青色のマスの位置を取得
    blue = [0] * (N + 1)
    for i in range(M):
        blue[A[i]] = 1
    # 青色のマスの間隔を取得
    interval = []
    cnt = 0
    for i in range(1, N + 1):
        if blue[i] == 1:
            if cnt != 0:
                interval.append(cnt)
            cnt = 0
        else:
            cnt += 1
    if cnt != 0:
        interval.append(cnt)
    # 青色のマスの間隔が2以上の場合、間隔の最小値を取得
    if len(interval) == 0:
        print(0)
    elif len(interval) == 1:
        print(1)
    else:
        min_interval = min(interval)
        if min_interval == 1:
            print(2)
        else:
            print((min_interval + 1) // 2)

if __name__ == '__main__':
    main()