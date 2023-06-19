def get_min_xor(n, a):
    min_xor = 2**30
    for i in range(1, n):
        xor = a[i-1]^a[i]
        if xor < min_xor:
            min_xor = xor
    return min_xor

if __name__ == '__main__':
    get_min_xor()