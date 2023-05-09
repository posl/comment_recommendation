def main():
    N = int(input())
    N_bin = bin(N)[2:]
    N_bin_len = len(N_bin)
    N_bin_1_pos = [i for i, x in enumerate(N_bin) if x == '1']
    for i in range(2**len(N_bin_1_pos)):
        x_bin = bin(i)[2:]
        x_bin = '0'*(len(N_bin_1_pos) - len(x_bin)) + x_bin
        x_bin_1_pos = [i for i, x in enumerate(x_bin) if x == '1']
        if set(x_bin_1_pos).issubset(set(N_bin_1_pos)):
            x_bin = '0'*(N_bin_len - len(x_bin)) + x_bin
            print(int(x_bin, 2))
