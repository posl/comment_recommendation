def main():
    # 入力
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    # 操作前の A の要素の総和
    S = sum(A)
    # 操作後の A の要素の総和の最小値
    ans = 10**18
    # x を 0 から N まで試す
    for x in range(N+1):
        # x として 0 を選んだ場合
        if x == 0:
            # 操作後の A の要素の総和
            T = S
            # y を 0 から N まで試す
            for y in range(N+1):
                # y として 0 を選んだ場合
                if y == 0:
                    # 操作後の A の要素の総和の最小値を更新
                    ans = min(ans, T)
                # y として 1 以上の整数を選んだ場合
                else:
                    # 操作後の A の要素の総和
                    T += R - A[N-y]
                    # 操作後の A の要素の総和の最小値を更新
                    ans = min(ans, T)
        # x として 1 以上の整数を選んだ場合
        else:
            # 操作後の A の要素の総和
            T = S + L * x - sum(A[:x])
            # y を 0 から N まで試す
            for y in range(N+1):
                # y として 0 を選んだ場合
                if y == 0:
                    # 操作後の A の要素の総和の最小値を更新
                    ans = min(ans, T)
                # y として 1 以上の整数を選んだ場合
                else:
                    # 操作後の A の要素の総和
                    T += R - A[N-y]
                    # 操作後の
