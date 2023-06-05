def bit_sum(a, s):
    if a > s:
        return False
    if a == 0:
        return s == 0
    if s == 0:
        return False
    if a == s:
        return True
    if a & s != a:
        return False
    return bit_sum(a >> 1, s >> 1)
