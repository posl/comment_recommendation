def get_xor(a, b):
    if a == b:
        return a
    else:
        return get_xor(a, b-1) ^ b
