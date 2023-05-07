def main():
    import sys
    from collections import defaultdict
    from bisect import bisect_left
    # # for debug
    # f = open("input.txt", "r")
    # sys.stdin = f
    N, W = map(int, input().split())
    cheese = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[0])
    # 重さをiとしたとき、価値の最大値を記録する
    dp = defaultdict(int)
    # 重さ0のときの価値は0
    dp[0] = 0
    # 重さ1~Wのときの価値を記録する
    for i in range(1, W+1):
        # 重さiに対応する価値の初期値は0
        dp[i] = 0
        # 価値の最大値を探す
        for j in range(N):
            # 重さi以下であれば、価値を計算する
            if cheese[j][0] <= i:
                # 価値が最大値を超えていれば、更新する
                if dp[i] < dp[i-cheese[j][0]] + cheese[j][0] * cheese[j][1]:
                    dp[i] = dp[i-cheese[j][0]] + cheese[j][0] * cheese[j][1]
            # 重さiより大きい場合は、価値は計算する必要がない
            else:
                break
    print(dp[W])
