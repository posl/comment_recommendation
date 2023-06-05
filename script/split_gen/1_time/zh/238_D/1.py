def get_bit_sum(a,s):
    res = 0
    while s > 0:
        res += s & 1
        s = s >> 1
    return res
