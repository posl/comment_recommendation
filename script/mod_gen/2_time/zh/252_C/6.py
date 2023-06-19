def solve():
    N = int(input())
    S = [input() for _ in range(N)]
    # 1つ目のリールのボタンを押す回数を全探索する
    ans = 10 ** 100
    for i in range(10):
        # 各リールのボタンを押す回数を記録する配列
        cnt = [0] * N
        # 1つ目のリールのボタンを押す回数
        cnt[0] = i
        # 各リールのボタンを押す回数を決める
        for j in range(1, N):
            # 1つ前のリールのボタンを押す回数
            cnt[j] = (10 + int(S[j - 1][j - 1]) - cnt[j - 1]) % 10
        # 各リールのボタンを押す回数を全て決めたときの合計時間
        sum_cnt = sum(cnt)
        # 合計時間が最小の場合は、その時間を解とする
        if ans > sum_cnt:
            ans = sum_cnt
    print(ans)

if __name__ == '__main__':
    solve()