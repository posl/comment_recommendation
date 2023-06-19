def bit_and(a, s):
    if a > s:
        return False
    if a == s:
        return True
    if a == 0:
        return bit_and(a, s-1)
    if a == 1:
        return bit_and(a, s-1)
    if (a & 1) == 1 and (s & 1) == 1:
        return bit_and(a>>1, s>>1)
    else:
        return False

if __name__ == '__main__':
    bit_and()