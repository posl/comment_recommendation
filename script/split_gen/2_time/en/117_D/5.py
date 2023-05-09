def solve(n, k, a):
    # a XOR b = c
    # a XOR c = b
    # b XOR c = a
    # a + b + c = 0
    # a + b = -c
    # a = -c - b
    # 0 <= a <= k
    # 0 <= k <= 10 ** 12
    # 0 <= a <= 10 ** 12
    # a + b = -c
    # a + b = -c
    # a + b = -a - b
    # 2 * a + b = 0
    # b = -2 * a
    # 0 <= b <= k
    # 0 <= -2 * a <= k
    # 0 <= -a <= k / 2
    # 0 <= a <= k / 2
    # a + b = -c
    # a + b = -a - b
    # b = -c - a
    # b = -a - a
    # b = -2 * a
    # 0 <= b <= k
    # 0 <= -2 * a <= k
    # 0 <= -a <= k / 2
    # 0 <= a <= k / 2
    # a + b = -c
    # a + b = -a - b
    # a = -c - b
    # a = -b - b
    # a = -2 * b
    # 0 <= a <= k
    # 0 <= -2 * b <= k
    # 0 <= -b <= k / 2
    # 0 <= b <= k / 2
    # a + b = -c
    # a + b = -a - b
    # a = -c - b
    # b = -c - a
    # a = -b - b
    # b = -a - a
    # a = -2 * b
    # b = -2 * a
    # 0 <= a <= k
    # 0 <= -2 * b <= k
    # 0 <= -b <= k / 2
    # 0 <= b <= k / 2
    # a
