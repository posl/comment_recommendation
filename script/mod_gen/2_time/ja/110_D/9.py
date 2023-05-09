def calc_comb(n, r):
    """
    nCrを計算する関数
    """
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

if __name__ == '__main__':
    calc_comb()