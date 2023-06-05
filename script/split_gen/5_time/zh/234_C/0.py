def get_number(k):
    k -= 1
    k_bin = bin(k)[2:]
    k_bin = k_bin.replace('1','2')
    k_bin = k_bin.replace('0','1')
    k_bin = k_bin.replace('2','0')
    return int(k_bin)
