def get_bit_and(a, b):
    result = 0
    for i in range(60):
        if a & b & (1 << i):
            result += 1 << i
    return result
