def xor_sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] ^ xor_sum(arr[1:])
