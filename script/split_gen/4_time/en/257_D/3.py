def main():
    N = int(input())
    trampolines = []
    for i in range(N):
        x, y, p = map(int, input().split())
        trampolines.append((x, y, p))
    # print(trampolines)
    # 二分探索
    # Sの最大値を求める。Sが大きいほど、P_iSの値も大きくなる
    # Sの最大値を求めるために、Sの最大値の範囲を二分探索で狭めていく
    # Sの最大値の範囲は、0 ~ 10**9となる
    # Sの最大値の範囲を狭めるために、二分探索を行う
    # 二分探索の条件は、Sの最大値がmid以下の場合に、すべてのトランポリンに到達できるかどうかを判定する
    # すべてのトランポリンに到達できる場合、Sの最大値の範囲を狭める
    # すべてのトランポリンに到達できない場合、Sの最大値の範囲を広げる
    # 二分探索の初期値
    left = 0
    right = 10**9
    while right - left > 1:
        mid = (left + right) // 2
        # print('left, right, mid', left, right, mid)
        # すべてのトランポリンに到達できるかどうかを判定する
        # すべてのトランポリンに到達できる場合、Sの最大値の範囲を狭める
        # すべてのトランポリンに到達できない場合、Sの最大
