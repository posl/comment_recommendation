def get_xor(a, b):
    if a == b:
        return a
    else:
        return get_xor(a, b-1) ^ b

if __name__ == '__main__':
    get_xor()