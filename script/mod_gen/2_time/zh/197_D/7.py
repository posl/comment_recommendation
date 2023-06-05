def bit_or(*args):
    res = 0
    for i in args:
        res |= i
    return res

if __name__ == '__main__':
    bit_or()