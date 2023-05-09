def main():
    S = input()
    MOD = 10**9 + 7
    A = S.count('A')
    B = S.count('B')
    C = S.count('C')
    Q = S.count('?')
    # 3^Q
    three_Q = pow(3, Q, MOD)
    # 3^Q - 1
    three_Q_minus_1 = (three_Q - 1) % MOD
    # 3^Q - 1 / 2
    three_Q_minus_1_div_2 = pow(three_Q_minus_1, MOD - 2, MOD)
    # 3^Q - 1 / 2 * A
    A_ = (three_Q_minus_1_div_2 * A) % MOD
    # 3^Q - 1 / 2 * B
    B_ = (three_Q_minus_1_div_2 * B) % MOD
    # 3^Q - 1 / 2 * C
    C_ = (three_Q_minus_1_div_2 * C) % MOD
    # 3^Q - 1 / 2 * A * B
    AB = (A_ * B_) % MOD
    # 3^Q - 1 / 2 * B * C
    BC = (B_ * C_) % MOD
    # 3^Q - 1 / 2 * C * A
    CA = (C_ * A_) % MOD
    # 3^Q - 1 / 2 * A * B * C
    ABC = (AB * C_) % MOD
    # 3^Q - 1 / 2 * A + 3^Q - 1 / 2 * B + 3^Q - 1 / 2 * C - 3^Q - 1 / 2 * A * B - 3^Q - 1 / 2 * B * C - 3^Q - 1 / 2 * C * A + 3^Q - 1 / 2 * A * B * C
    print((A_ + B_ + C_ - AB - BC - CA + ABC) % MOD)
