def next_permutation(a):
    N = len(a)
    # 1. a[i - 1] < a[i] を満たす最大の i を求める
    i = N - 1
    while i > 0 and a[i - 1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    # 2. a[j] > a[i - 1] を満たす最大の j を求める
    j = N - 1
    while a[j] <= a[i - 1]:
        j -= 1
    # 3. a[i - 1] と a[j] を交換
    a[i - 1], a[j] = a[j], a[i - 1]
    # 4. a[i] 以降を反転
    j = N - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True
