def solve():
    N = int(input())
    T = [0] * N
    X = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], X[i], A[i] = map(int, input().split())
    # 各穴に出てくる最大のすぬけ君の大きさを求める
    # すぬけ君は時刻順に出てくるため、時刻が同じ場合は大きい方を採用する
    max_A = [0] * 5
    for i in range(N):
        max_A[X[i]] = max(max_A[X[i]], A[i])
    # 時刻 0 から 4 までの移動時間を求める
    # 移動時間は、移動先の座標の差分の絶対値
    # ただし、移動時間が 1 未満の場合は 1 とする
    move_time = [0] * 5
    for i in range(4):
        move_time[i+1] = max(1, abs(i - (i+1)))
    # 移動時間と穴に出てくる最大のすぬけ君の大きさを掛け合わせたものの合計が答え
    ans = 0
    for i in range(5):
        ans += max_A[i] * move_time[i]
    print(ans)

if __name__ == '__main__':
    solve()