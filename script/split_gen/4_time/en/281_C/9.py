def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    # t = 0 から t までの合計時間
    sum_a = sum(a)
    # t を sum_a で割った余り
    t = t % sum_a
    # t が 0 になったら n 番目の曲が再生されている
    if t == 0:
        print(n)
        return
    # t が 0 でない場合
    for i in range(n):
        # t が a[i] 以下になったら i + 1 番目の曲が再生されている
        if t <= a[i]:
            print(i + 1, t)
            return
        else:
            # t が a[i] を超える場合は、a[i] を引いて t を更新する
            t -= a[i]
