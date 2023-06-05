def compute_xor(x, y):
    x_bin = bin(x)[2:]
    y_bin = bin(y)[2:]
    x_len = len(x_bin)
    y_len = len(y_bin)
    if x_len > y_len:
        y_bin = '0' * (x_len - y_len) + y_bin
    elif x_len < y_len:
        x_bin = '0' * (y_len - x_len) + x_bin
    result_bin = ''
    for i in range(len(x_bin)):
        result_bin += '1' if x_bin[i] != y_bin[i] else '0'
    return int(result_bin, 2)
