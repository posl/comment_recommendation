def main():
    n = int(input())
    n_bit = bin(n)[2:]
    n_len = len(n_bit)
    n_1 = [i for i, x in enumerate(n_bit) if x == "1"]
    for i in range(2**len(n_1)):
        bit = bin(i)[2:]
        bit = "0"*(len(n_1)-len(bit)) + bit
        bit = bit[::-1]
        bit = list(bit)
        n_bit_tmp = list(n_bit)
        for j in range(len(n_1)):
            n_bit_tmp[n_1[j]] = bit[j]
        print(int("".join(n_bit_tmp),2))
