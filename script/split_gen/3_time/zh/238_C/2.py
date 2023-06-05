def get_modulo_sum(N):
    # 998244353
    modulo = 998244353
    # 位数
    digit = len(str(N))
    # 位数が一桁の場合
    if digit == 1:
        return N
    # 位数が二桁以上の場合
    # 位数が一桁少ない桁数の最大値
    max_digit = int('9' * (digit - 1))
    # 位数が一桁少ない桁数の最大値までの和
    sum = 0
    for i in range(1, max_digit + 1):
        sum += i
    # 位数が一桁少ない桁数の最大値までの和に、位数が一桁少ない桁数の最大値をかける
    sum *= max_digit
    # 位数が一桁少ない桁数の最大値までの和に、位数が一桁少ない桁数の最大値までの和を足す
    sum += get_modulo_sum(max_digit)
    # 位数が一桁少ない桁数の最大値までの和に、位数が一桁少ない桁数の最大値までの和を足す
    sum %= modulo
    # 位数が一桁少ない桁数の最大値に、Nと位数が一桁少ない桁数の最大値の差をかける
    sum += max_digit * (N - max_digit)
    # 位数が一桁少ない桁数の最大値に、Nと位数が一桁少ない桁数の最大値の差を足す
    sum %= modulo
    # 位数が一桁少ない桁数の最大値に、Nと位数が一桁少ない桁数の最大値の差を足す
    sum += get_mod
