def calc_combination(a, b):
    """
    a + b 個から a 個を選ぶ組み合わせの数を返す
    """
    # a + b 個から b 個を選ぶ組み合わせの数を返す
    if a < b:
        return calc_combination(b, a)
    # 分子
    numerator = 1
    for i in range(a + 1, a + b + 1):
        numerator *= i
    # 分母
    denominator = 1
    for i in range(1, b + 1):
        denominator *= i
    return numerator // denominator
