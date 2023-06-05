def xor(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return a ^ b

if __name__ == '__main__':
    xor()