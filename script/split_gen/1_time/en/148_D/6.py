def main():
    N = int(input())
    a = list(map(int, input().split()))
    # 最小値を求める
    min_a = min(a)
    # 最小値のindexを求める
    min_a_index = a.index(min_a)
    # 最小値のindexより左側の値を切り取る
    a = a[min_a_index:]
    # 最小値のindexより右側の値を切り取る
    a = a[:N]
    # 最小値からNまでの値を求める
    min_a_to_N = list(range(min_a, N + 1))
    # 最小値からNまでの値とaの値が一致しているかを確認する
    if min_a_to_N == a:
        print(min_a_index)
    else:
        print(-1)
