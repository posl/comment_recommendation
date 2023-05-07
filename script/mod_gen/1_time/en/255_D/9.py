def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    # 1回の操作で最大でどれだけ変化するか
    max_change = max(a) - min(a)
    # xの最大値が変化する最大値を超えている場合は、xの最大値を最大値にする
    if max(x) > max_change:
        max_change = max(x)
    # aの最小値を引いたものが、xの最小値よりも大きい場合は、xの最小値を最小値にする
    if min(a) - min(x) > 0:
        min_change = min(x)
    else:
        min_change = min(a) - min(x)
    # xの最小値を引いたものが、aの最大値よりも小さい場合は、xの最大値を最大値にする
    if max(a) - max(x) < 0:
        max_change = max(x)
    # aの最小値を引いたものが、xの最大値よりも大きい場合は、xの最小値を最小値にする
    if min(a) - min(x) > 0:
        min_change = min(x)
    # aの最大値を引いたものが、xの最小値よりも小さい場合は、xの最大値を最大値にする
    if max(a) - max(x) < 0:
        max_change = max(x)
    # aの最小値を引いたものが、xの最大値よりも大きい場合は、xの最小値を最小値にする
    if min(a) - min(x) > 0:
        min_change = min(x)
    # aの最大値を引いたものが、xの最小値よりも小さい場合は、

if __name__ == '__main__':
    main()