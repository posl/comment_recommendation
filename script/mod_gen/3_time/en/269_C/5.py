def main():
    N = int(input())
    N_bin = bin(N)[2:]
    N_len = len(N_bin)
    #print(N_bin, N_len)
    for i in range(2**N_len):
        i_bin = bin(i)[2:]
        i_len = len(i_bin)
        #print(i_bin, i_len)
        if i_len > N_len:
            break
        if all([N_bin[N_len - 1 - j] == i_bin[i_len - 1 - j] for j in range(i_len) if i_bin[i_len - 1 - j] == '1']):
            print(i)

if __name__ == '__main__':
    main()