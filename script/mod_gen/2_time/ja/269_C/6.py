def main():
    N = int(input())
    if N == 0:
        print(0)
        exit()
    # print(N)
    N_bin = bin(N)[2:]
    # print(N_bin)
    N_bin = N_bin[::-1]
    # print(N_bin)
    N_bin_list = list(N_bin)
    # print(N_bin_list)
    N_bin_list = [int(i) for i in N_bin_list]
    # print(N_bin_list)
    N_bin_list_len = len(N_bin_list)
    # print(N_bin_list_len)
    for i in range(2**N_bin_list_len):
        # print(i)
        i_bin = bin(i)[2:]
        # print(i_bin)
        i_bin = i_bin[::-1]
        # print(i_bin)
        i_bin_list = list(i_bin)
        # print(i_bin_list)
        i_bin_list = [int(j) for j in i_bin_list]
        # print(i_bin_list)
        i_bin_list_len = len(i_bin_list)
        # print(i_bin_list_len)
        if i_bin_list_len > N_bin_list_len:
            break
        for k in range(i_bin_list_len):
            # print(k)
            if i_bin_list[k] == 1 and N_bin_list[k] == 0:
                break
        else:
            print(i)

if __name__ == '__main__':
    main()