def main():
    # 读入数据
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    # 模拟
    # 歌曲循环播放
    # 当前播放的歌曲编号
    cur = 0
    # 当前播放的歌曲已经播放的时间
    cur_time = 0
    while cur_time + a[cur] <= t:
        cur_time += a[cur]
        cur += 1
        if cur == n:
            cur = 0
    print(cur + 1, cur_time)

if __name__ == '__main__':
    main()