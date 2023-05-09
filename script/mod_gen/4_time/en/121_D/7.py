def xor(a, b):
    if a == b:
        return a
    else:
        return xor(a, b-1) ^ b

if __name__ == '__main__':
    xor()