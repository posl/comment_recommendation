def main():
    N = int(input())
    N_bin = bin(N)[2:]
    N_len = len(N_bin)
    result = []
    for i in range(2**N_len):
        i_bin = bin(i)[2:]
        i_len = len(i_bin)
        if i_len > N_len:
            break
        if i_len < N_len:
            i_bin = '0'*(N_len-i_len) + i_bin
        for j in range(N_len):
            if i_bin[j] == '1' and N_bin[j] == '0':
                break
        else:
            result.append(i)
    print(*result, sep='\n')

if __name__ == '__main__':
    main()