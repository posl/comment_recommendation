def solve():
    N = int(input())
    P = list(map(int, input().split()))
    # 人iが幸福かどうかを表す値
    # 0: 不幸
    # 1: 幸福
    # 2: 未定
    status = [2] * N
    # 幸福な人の数
    happy_count = 0
    while True:
        # 幸福な人の数を更新
        happy_count += status.count(1)
        # 幸福な人の数が変わらなかったら終了
        if happy_count == N:
            break
        # 幸福な人の数を更新
        happy_count = 0
        # 人iが幸福かどうかを更新
        for i in range(N):
            if status[i] == 1:
                continue
            # 人iの前の人の番号
            prev = (i - 1 + N) % N
            # 人iの後ろの人の番号
            next = (i + 1) % N
            # 人iの前の人が幸福なら人iは幸福
            if status[prev] == 1:
                status[i] = 1
            # 人iの後ろの人が幸福なら人iは幸福
            elif status[next] == 1:
                status[i] = 1
        # 転置
        P = [P[p] for p in P]
    # 幸福な人の数を出力
    print(happy_count)

if __name__ == '__main__':
    solve()