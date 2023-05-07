def main():
    N = int(input())
    N_bin = bin(N)[2:][::-1]
    N_bin_len = len(N_bin)
    for i in range(2**N_bin_len):
        i_bin = bin(i)[2:][::-1]
        i_bin_len = len(i_bin)
        for j in range(i_bin_len):
            if i_bin[j] == '1' and N_bin[j] != '1':
                break
        else:
            print(i)

if __name__ == '__main__':
    main()