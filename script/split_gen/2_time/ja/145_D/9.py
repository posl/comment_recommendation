def make_mod_combination(n, mod):
    # mod で割った余りの階乗のリストを返す
    # n: 階乗の上限
    # mod: 余り
    fac = [1]
    for i in range(1, n+1):
        fac.append(fac[-1] * i % mod)
    return fac
