def main():
    n = int(input())
    n_bin = bin(n)[2:]
    n_bin_len = len(n_bin)
    n_bin_1 = [i for i, x in enumerate(n_bin) if x == '1']
    ans = []
    for i in range(2**n_bin_len):
        i_bin = bin(i)[2:]
        i_bin_1 = [i for i, x in enumerate(i_bin) if x == '1']
        if all(x in n_bin_1 for x in i_bin_1):
            ans.append(i)
    for a in ans:
        print(a)

if __name__ == '__main__':
    main()