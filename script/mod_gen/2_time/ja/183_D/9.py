def main():
    N, W = map(int, input().split())
    # お湯を使う人の時間帯を管理するリスト
    time = []
    for _ in range(N):
        S, T, P = map(int, input().split())
        time.append((S, P))
        time.append((T, -P))
    # 時間帯を時刻順にソート
    time.sort()
    # お湯を使う人の時間帯を管理するリスト
    now = 0
    for _, P in time:
        now += P
        if now > W:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()