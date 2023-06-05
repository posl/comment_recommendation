def get_min_xor(a, n):
    min_xor = 2**30
    for i in range(0, n-1):
        for j in range(i+1, n):
            xor = a[i] ^ a[j]
            if xor < min_xor:
                min_xor = xor
    return min_xor

if __name__ == '__main__':
    get_min_xor()