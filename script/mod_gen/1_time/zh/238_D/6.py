def get_bit_sum(a, s):
    if a > s:
        return False
    if a == s:
        return True
    if (a & s) == a:
        return True
    if (a & s) == s:
        return True
    return False

if __name__ == '__main__':
    get_bit_sum()