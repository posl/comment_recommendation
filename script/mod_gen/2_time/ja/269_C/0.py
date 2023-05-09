def main():
    N = int(input())
    N_bin = bin(N)[2:]
    N_bin = N_bin[::-1]
    for i in range(2 ** len(N_bin)):
        i_bin = bin(i)[2:]
        i_bin = i_bin[::-1]
        if len(i_bin) < len(N_bin):
            i_bin += '0' * (len(N_bin) - len(i_bin))
        if all([i_bin[j] == '0' or N_bin[j] == '1' for j in range(len(N_bin))]):
            print(i)

if __name__ == '__main__':
    main()