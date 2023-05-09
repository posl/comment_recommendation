def main():
    N = int(input())
    # 区間の始点、終点、区間の種類を格納する配列
    intervals = [[0]*4 for i in range(N)]
    for i in range(N):
        intervals[i] = list(map(int, input().split()))
    # 区間の始点、終点、区間の種類をそれぞれ昇順にソートする
    intervals.sort(key=lambda x: (x[1], x[0], x[2]))
    # 区間の種類ごとに、始点と終点のリストを作成する
    intervals_start = [[], [], [], []]
    intervals_end = [[], [], [], []]
    for i in range(N):
        intervals_start[intervals[i][0]-1].append(intervals[i][1])
        intervals_end[intervals[i][0]-1].append(intervals[i][2])
    # 区間の種類ごとに、始点と終点のリストを昇順にソートする
    for i in range(4):
        intervals_start[i].sort()
        intervals_end[i].sort()
    # 重複する区間の個数をカウントする
    cnt = 0
    for i in range(N):
        # 区間の種類を取り出す
        t = intervals[i][0]
        # 区間の終点を取り出す
        r = intervals[i][2]
        # 区間の種類が1,2の場合
        if t == 1 or t == 2:
            # 区間の終点より大きい始点の個数をカウントする
            cnt += len(intervals_start[0]) - bisect.bisect_left(intervals_start[0], r)
            cnt += len(intervals_start[1]) - bisect.bisect_left(intervals_start[1], r)
            # 区間の終点より大きい終点の個数をカウントする
            cnt += len(intervals_end[2]) - bisect.bisect

if __name__ == '__main__':
    main()