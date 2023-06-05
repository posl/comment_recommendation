def find_min_xor(n, arr):
    min_xor = 2**30
    for i in range(n):
        for j in range(i+1, n):
            xor = arr[i] ^ arr[j]
            if xor < min_xor:
                min_xor = xor
    return min_xor

if __name__ == '__main__':
    find_min_xor()